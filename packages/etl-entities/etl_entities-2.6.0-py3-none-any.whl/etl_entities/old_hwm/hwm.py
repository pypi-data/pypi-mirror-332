# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime
from typing import Generic, TypeVar

try:
    from pydantic.v1 import Field, validate_model
except (ImportError, AttributeError):
    from pydantic import Field, validate_model  # type: ignore[no-redef, assignment]

from etl_entities.entity import Entity, GenericModel
from etl_entities.hwm import HWMTypeRegistry
from etl_entities.process import Process, ProcessStackManager

ValueType = TypeVar("ValueType")
SerializedType = TypeVar("SerializedType")


class HWM(ABC, Entity, GenericModel, Generic[ValueType, SerializedType]):
    """Generic HWM type

    .. deprecated:: 2.0.0
        Use :obj:`etl_entities.hwm.HWM` instead

    Parameters
    ----------
    value : Any

        HWM value of any type

    modified_time : :obj:`datetime.datetime`, default: current datetime

        HWM value modification time

    process : :obj:`etl_entities.process.process.Process`, default: current process

        Process instance
    """

    source: Entity
    value: ValueType
    modified_time: datetime = Field(default_factory=datetime.now)
    process: Process = Field(default_factory=ProcessStackManager.get_current)

    def set_value(self, value: ValueType) -> HWM:
        """Replaces current HWM value with the passed one, and return HWM.

        .. note::

            Changes HWM value in place instead of returning new one

        Returns
        -------
        result : HWM

            Self

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import IntHWM

            old_hwm = IntHWM(value=1, ...)

            old_hwm.set_value(2)
            assert old_hwm.value == 2
        """

        new_value = self._check_new_value(value)

        if self.value != new_value:
            object.__setattr__(self, "value", new_value)  # noqa: WPS609
            object.__setattr__(self, "modified_time", datetime.now())  # noqa: WPS609

        return self

    def serialize(self) -> dict:
        """Return dict representation of HWM

        Returns
        -------
        result : dict

            Serialized HWM

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import IntHWM

            old_hwm = IntHWM(value=1, ...)
            assert old_hwm.serialize() == {
                "value": "1",
                "type": "int",
                "column": {"name": ..., "partition": ...},
                "source": ...,
                "process": ...,
            }
        """

        result = json.loads(self.json())
        result["type"] = HWMTypeRegistry.get_key(self.__class__)  # type: ignore
        result["value"] = self.serialize_value()
        return result

    @classmethod
    def deserialize(cls, inp: dict):
        """Return HWM from dict representation

        Returns
        -------
        result : HWM

            Deserialized HWM

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import IntHWM

            assert IntHWM.deserialize(
                {
                    "value": "1",
                    "type": "int",
                    "column": {"name": ..., "partition": ...},
                    "source": ...,
                    "process": ...,
                }
            ) == IntHWM(value=1, ...)

            IntHWM.deserialize({"type": "date"})  # raises ValueError
        """

        value = deepcopy(inp)
        return super().deserialize(value)

    @abstractmethod
    def serialize_value(self) -> SerializedType:
        """Return string representation of HWM value

        Returns
        -------
        result : json

            Serialized value

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import HWM

            old_hwm = HWM(value=1, ...)
            assert old_hwm.serialize_value() == "1"
        """

    @abstractmethod
    def covers(self, value) -> bool:
        """Return ``True`` if input value is already covered by HWM"""

    @abstractmethod
    def update(self, value):
        """Update current HWM value with some implementation-specific logic, and return HWM"""

    def _check_new_value(self, value):
        validated_dict, _, validation_error = validate_model(
            self.__class__,
            self.copy(update={"value": value}).__dict__,
        )
        if validation_error:
            raise validation_error

        return validated_dict["value"]
