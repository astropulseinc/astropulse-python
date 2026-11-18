# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ModelFormat(str, Enum):
    """
    ModelFormat
    """

    """
    allowed enum values
    """
    VLLM = 'vLLM'
    SKLearn = 'SKLearn'
    XGBoost = 'XGBoost'
    LightGBM = 'LightGBM'
    TensorFlow = 'TensorFlow'
    PyTorch = 'PyTorch'
    ONNX = 'ONNX'
    TensorRT = 'TensorRT'
    Triton = 'Triton'
    MLflow = 'MLflow'
    PMML = 'PMML'
    Paddle = 'Paddle'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModelFormat from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        """Accept a value this version does not know, keeping it as given.

        The API may add values to this enum at any time. One this version does
        not list parses to a member whose ``value`` is the string received, so
        it is never lost and is sent back unchanged; it equals no listed member.
        """
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = str(value)
        member._value_ = value
        return member

    @property
    def label(self) -> str | None:
        """The display name the API document gives this value.

        ``None`` for a value this version of the package does not list.
        """
        return _LABELS.get(self._value_)

    @property
    def description(self) -> str | None:
        """What this value means, as the API document describes it.

        ``None`` for a value this version of the package does not list.
        """
        return _DESCRIPTIONS.get(self._value_)

    @classmethod
    def label_for(cls, value: str) -> str | None:
        """The display name of a value, or ``None`` for one this version does not list."""
        return _LABELS.get(value)

    @classmethod
    def description_for(cls, value: str) -> str | None:
        """What a value means, or ``None`` for one this version does not list."""
        return _DESCRIPTIONS.get(value)



# The API document lists the labels and descriptions in the order of the values,
# which is also the order of the members above.
_LABELS: dict[str, str] = dict(zip(
    [member._value_ for member in ModelFormat],
    [
        "vLLM",
        "scikit-learn",
        "XGBoost",
        "LightGBM",
        "TensorFlow",
        "PyTorch",
        "ONNX",
        "TensorRT",
        "Triton",
        "MLflow",
        "PMML",
        "PaddlePaddle",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in ModelFormat],
    [
        "A generative model, such as a Hugging Face language model, served by vLLM with an OpenAI-compatible API.",
        "A model saved by scikit-learn.",
        "A model saved by XGBoost.",
        "A model saved by LightGBM.",
        "A TensorFlow SavedModel.",
        "A PyTorch model packaged for TorchServe.",
        "A model in the Open Neural Network Exchange format.",
        "A model compiled with NVIDIA TensorRT.",
        "A model repository for NVIDIA Triton Inference Server.",
        "A model saved in the MLflow model format.",
        "A model in the Predictive Model Markup Language.",
        "A model saved by PaddlePaddle.",
    ],
))

