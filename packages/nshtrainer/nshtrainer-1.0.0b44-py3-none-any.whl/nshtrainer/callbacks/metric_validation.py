from __future__ import annotations

import logging
from typing import Literal

from lightning.pytorch.utilities.exceptions import MisconfigurationException
from typing_extensions import final, override, assert_never

from .._callback import NTCallbackBase
from ..metrics import MetricConfig
from .base import CallbackConfigBase, callback_registry

log = logging.getLogger(__name__)


@final
@callback_registry.register
class MetricValidationCallbackConfig(CallbackConfigBase):
    name: Literal["metric_validation"] = "metric_validation"

    error_behavior: Literal["raise", "warn"] = "raise"
    """
    Behavior when an error occurs during validation:
    - "raise": Raise an error and stop the training.
    - "warn": Log a warning and continue the training.
    """

    validate_default_metric: bool = True
    """Whether to validate the default metric from the root config."""

    metrics: list[MetricConfig] = []
    """List of metrics to validate."""

    @override
    def create_callbacks(self, trainer_config):
        metrics = self.metrics.copy()
        if (
            self.validate_default_metric
            and (default_metric := trainer_config.primary_metric) is not None
        ):
            metrics.append(default_metric)

        yield MetricValidationCallback(self, metrics)


class MetricValidationCallback(NTCallbackBase):
    def __init__(
        self, config: MetricValidationCallbackConfig, metrics: list[MetricConfig]
    ):
        super().__init__()

        self.config = config
        self.metrics = metrics

    @override
    def on_sanity_check_end(self, trainer, pl_module):
        super().on_sanity_check_end(trainer, pl_module)

        log.debug("Validating metrics...")
        logged_metrics = set(trainer.logged_metrics.keys())
        for metric in self.metrics:
            if metric.validation_monitor in logged_metrics:
                continue

            match self.config.error_behavior:
                case "raise":
                    raise MisconfigurationException(
                        f"Metric '{metric.validation_monitor}' not found in logged metrics."
                    )
                case "warn":
                    log.warning(
                        f"Metric '{metric.validation_monitor}' not found in logged metrics."
                    )
                case _:
                    assert_never(self.config.error_behavior)
