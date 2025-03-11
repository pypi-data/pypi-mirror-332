"""
Trainer :class:`Callback` implementations.
"""

from .beaker import BeakerCallback
from .callback import Callback, CallbackConfig
from .checkpointer import CheckpointerCallback, CheckpointRemovalStrategy
from .comet import CometCallback, CometNotificationSetting
from .config_saver import ConfigSaverCallback
from .console_logger import ConsoleLoggerCallback
from .evaluator_callback import (
    DownstreamEvaluatorCallbackConfig,
    EvaluatorCallback,
    LMEvaluatorCallbackConfig,
)
from .float8_handler import Float8HandlerCallback
from .garbage_collector import GarbageCollectorCallback
from .gpu_memory_monitor import GPUMemoryMonitorCallback
from .grad_clipper import GradClipperCallback
from .matrix_normalizer import MatrixNormalizerCallback
from .moe_handler import MoEHandlerCallback
from .profiler import ProfilerCallback
from .scheduler import SchedulerCallback
from .sequence_length_scheduler import SequenceLengthSchedulerCallback
from .slack_notifier import SlackNotificationSetting, SlackNotifierCallback
from .speed_monitor import SpeedMonitorCallback
from .wandb import WandBCallback

__all__ = [
    "Callback",
    "CallbackConfig",
    "CheckpointerCallback",
    "CheckpointRemovalStrategy",
    "CometCallback",
    "CometNotificationSetting",
    "ConfigSaverCallback",
    "ConsoleLoggerCallback",
    "EvaluatorCallback",
    "Float8HandlerCallback",
    "LMEvaluatorCallbackConfig",
    "DownstreamEvaluatorCallbackConfig",
    "MoEHandlerCallback",
    "GarbageCollectorCallback",
    "GPUMemoryMonitorCallback",
    "GradClipperCallback",
    "MatrixNormalizerCallback",
    "ProfilerCallback",
    "SlackNotifierCallback",
    "SlackNotificationSetting",
    "SchedulerCallback",
    "SequenceLengthSchedulerCallback",
    "SpeedMonitorCallback",
    "WandBCallback",
    "BeakerCallback",
]

__doc__ += "\n"
for name in __all__[2:]:
    if name.endswith("Callback"):
        __doc__ += f"- :class:`{name}`\n"
