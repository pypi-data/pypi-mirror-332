from typing import Dict, List, Optional

import requests
from requests import HTTPError
from urllib3.util import retry

from databricks import version
from databricks.rag_eval import context, env_vars, session
from databricks.rag_eval.clients import databricks_api_client
from databricks.rag_eval.clients.managedrag import proto_serde
from databricks.rag_eval.config import assessment_config
from databricks.rag_eval.evaluation import (
    custom_metrics as agent_custom_metrics,
)
from databricks.rag_eval.evaluation import (
    entities,
    per_run_metrics,
)
from databricks.rag_eval.utils import request_utils

SESSION_ID_HEADER = "eval-session-id"
BATCH_SIZE_HEADER = "eval-session-batch-size"
CLIENT_VERSION_HEADER = "eval-session-client-version"
CLIENT_NAME_HEADER = "eval-session-client-name"
JOB_ID_HEADER = "eval-session-job-id"
JOB_RUN_ID_HEADER = "eval-session-job-run-id"
MLFLOW_RUN_ID_HEADER = "eval-session-mlflow-run-id"
MONITORING_WHEEL_VERSION_HEADER = "eval-session-monitoring-wheel-version"
# List of retryable error codes from the judge service. These codes are for errors returned in a
# rating object, not HTTP errors.
RETRYABLE_JUDGE_ERROR_CODES = ["2001", "2003", "3001", "3003", "3004"]


def get_default_retry_config():
    return retry.Retry(
        total=env_vars.RAG_EVAL_LLM_JUDGE_MAX_HTTP_ERROR_RETRIES.get(),
        backoff_factor=env_vars.RAG_EVAL_LLM_JUDGE_BACKOFF_FACTOR.get(),
        status_forcelist=[429, 500, 502, 503, 504],
        backoff_jitter=env_vars.RAG_EVAL_LLM_JUDGE_BACKOFF_JITTER.get(),
        allowed_methods=frozenset(
            ["GET", "POST"]
        ),  # by default, it doesn't retry on POST
    )


def _get_eval_session_headers():
    """Constructs the request headers from the thread-local session."""
    headers = {
        CLIENT_VERSION_HEADER: version.VERSION,
        CLIENT_NAME_HEADER: env_vars.RAG_EVAL_EVAL_SESSION_CLIENT_NAME.get(),
        JOB_ID_HEADER: context.get_context().get_job_id(),
        JOB_RUN_ID_HEADER: context.get_context().get_job_run_id(),
        MLFLOW_RUN_ID_HEADER: context.get_context().get_mlflow_run_id(),
    }
    headers = request_utils.add_traffic_id_header(headers)

    # Pass the internal version of the monitoring wheel if it is set
    current_session = session.current_session()
    if current_session:
        headers[SESSION_ID_HEADER] = current_session.session_id
        if current_session.monitoring_wheel_version:
            headers[MONITORING_WHEEL_VERSION_HEADER] = (
                current_session.monitoring_wheel_version
            )
        if current_session.session_batch_size is not None:
            headers[BATCH_SIZE_HEADER] = str(current_session.session_batch_size)

    return headers


def is_retryable_judge_error(assessment_result: entities.AssessmentResult) -> bool:
    """
    Returns True if the given assessment result is a retryable judge error. For per-chunk
    assessments, at least one rating can be a retryable error to return True.
    """
    if isinstance(assessment_result, entities.PerRequestAssessmentResult):
        return assessment_result.rating.error_code is not None and (
            assessment_result.rating.error_code in RETRYABLE_JUDGE_ERROR_CODES
        )
    elif isinstance(assessment_result, entities.PerChunkAssessmentResult):
        return any(
            [
                rating.error_code is not None
                and (rating.error_code in RETRYABLE_JUDGE_ERROR_CODES)
                for rating in assessment_result.positional_rating.values()
            ]
        )
    return False


class ManagedRagClient(databricks_api_client.DatabricksAPIClient):
    """
    Client to interact with the managed-rag service (/chat-assessments).

    Note: this client reads the session from the current thread and uses it to construct the request headers.
      Make sure to construct this client in the same thread where the session is initialized.
    """

    def __init__(self):
        super().__init__(version="2.0")
        self.proto_serde = proto_serde.ChatAssessmentProtoSerde()

    def get_assessment(
        self,
        eval_item: entities.EvalItem,
        config: assessment_config.BuiltinAssessmentConfig,
    ) -> List[entities.AssessmentResult]:
        """
        Retrieves the assessment results from the LLM judge service for the given eval item and requested assessment
        """
        assessment_name = config.assessment_name
        request_json = self.proto_serde.construct_assessment_request_json(
            eval_item, assessment_name, config.examples, config.domain_instructions
        )

        assessment_result = []
        # There are two distinct types of retries for the judge service:
        # - Retry on retryable HTTP errors (set up in the request session)
        # - Retry on retryable judge errors, set up by the loop below
        for _ in range(env_vars.RAG_EVAL_LLM_JUDGE_MAX_JUDGE_ERROR_RETRIES.get()):
            with self.get_default_request_session(
                get_default_retry_config(), headers=_get_eval_session_headers()
            ) as session:
                resp = session.post(
                    self.get_method_url("/agents/chat-assessments"),
                    json=request_json,
                )

            if resp.status_code == requests.codes.ok:
                assessment_result = self.proto_serde.construct_assessment_result(
                    resp.json(),
                    config,
                )
                # If there are no retryable judge errors, return the result
                if not any(
                    is_retryable_judge_error(result) for result in assessment_result
                ):
                    break
            else:
                try:
                    resp.raise_for_status()
                except HTTPError as e:
                    return self.proto_serde.construct_assessment_error_result(
                        config,
                        resp.status_code,
                        e,
                    )

        return assessment_result

    def emit_chat_assessment_usage_event(
        self,
        custom_assessments: List[assessment_config.EvaluationMetricAssessmentConfig],
        num_questions: Optional[int],
    ):
        request_json = (
            self.proto_serde.construct_chat_assessment_usage_event_request_json(
                custom_assessments, num_questions
            )
        )
        # Use default retries. Don't need to use response
        with self.get_default_request_session(
            headers=_get_eval_session_headers()
        ) as session:
            session.post(
                self.get_method_url("/agents/chat-assessment-usage-events"),
                json=request_json,
            )

    def get_assessment_metric_definitions(
        self, assessment_names: List[str]
    ) -> Dict[str, assessment_config.AssessmentInputRequirementExpression]:
        """Retrieves the metric definitions for the given assessment names."""
        request_json = (
            self.proto_serde.construct_assessment_metric_definition_request_json(
                assessment_names
            )
        )

        with self.get_default_request_session(
            get_default_retry_config(), headers=_get_eval_session_headers()
        ) as session:
            resp = session.post(
                self.get_method_url("/agents/chat-assessment-definitions"),
                json=request_json,
            )

        if resp.status_code == requests.codes.ok:
            return self.proto_serde.construct_assessment_input_requirement_expressions(
                resp.json()
            )
        else:
            try:
                resp.raise_for_status()
            except HTTPError as e:
                raise e

    def emit_client_error_usage_event(self, error_message: str):
        with self.get_default_request_session(
            headers=_get_eval_session_headers()
        ) as session:
            session.post(
                self.get_method_url("/agents/evaluation-client-usage-events"),
                json=self.proto_serde.construct_client_usage_events_request_json(
                    usage_events=[
                        self.proto_serde.construct_client_error_usage_event_json(
                            error_message=error_message
                        )
                    ]
                ),
            )

    def emit_custom_metric_usage_event(
        self,
        *,
        custom_metrics: List[agent_custom_metrics.CustomMetric],
        eval_count: Optional[int],
        metric_stats: Optional[Dict[str, per_run_metrics.MetricAggregateData]] = None,
    ):
        # Use default retries. Don't need to use response
        with self.get_default_request_session(
            headers=_get_eval_session_headers()
        ) as session:
            session.post(
                self.get_method_url("/agents/evaluation-client-usage-events"),
                json=self.proto_serde.construct_client_usage_events_request_json(
                    usage_events=[
                        self.proto_serde.construct_custom_metric_usage_event_json(
                            custom_metrics=custom_metrics,
                            eval_count=eval_count,
                            metric_stats=metric_stats,
                        )
                    ]
                ),
            )
