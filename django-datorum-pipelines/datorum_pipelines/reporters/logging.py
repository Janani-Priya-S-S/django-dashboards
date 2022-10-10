from typing import Optional

from datorum_pipelines import BasePipelineReporter

from ..status import PipelineTaskStatus
from ..log import logger


class LoggingReporter(BasePipelineReporter):
    def report(
        self,
        pipeline_id: Optional[str],
        task_id: Optional[str],
        status: PipelineTaskStatus,
        message: str,
    ):
        if pipeline_id:
            logger.info(
                f"Pipeline {pipeline_id} changed to state {status.value}: {message}"
            )
        else:
            logger.info(
                f"Task {task_id} changed to state {status.value}: {message}"
            )
