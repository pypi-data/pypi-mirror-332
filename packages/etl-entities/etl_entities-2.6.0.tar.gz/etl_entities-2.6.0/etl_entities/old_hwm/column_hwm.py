# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from functools import total_ordering
from typing import Generic, Optional, TypeVar

from etl_entities.entity import GenericModel
from etl_entities.old_hwm.hwm import HWM
from etl_entities.source import Column, Table

ColumnValueType = TypeVar("ColumnValueType")


# see https://github.com/python/mypy/issues/5374#issuecomment-1071157357
@total_ordering  # type: ignore[misc]
class ColumnHWM(HWM[Optional[ColumnValueType], str], GenericModel, Generic[ColumnValueType]):
    """Base column HWM type

    .. deprecated:: 2.0.0
        Use :obj:`etl_entities.hwm.column.column_hwm.ColumnHWM>` instead

    Parameters
    ----------
    column : :obj:`etl_entities.source.db.column.Column`

        Column instance

    source : :obj:`etl_entities.source.db.table.Table`

        Table instance

    value : ``ColumnValueType`` or ``None``, default: ``None``

        HWM value

    modified_time : :obj:`datetime.datetime`, default: current datetime

        HWM value modification time

    process : :obj:`etl_entities.process.process.Process`, default: current process

        Process instance
    """

    column: Column
    source: Table
    value: Optional[ColumnValueType] = None

    @property
    def name(self) -> str:
        """
        HWM column name

        Returns
        -------
        value : str

            Column name

        Examples
        --------

        .. code:: python

            column = Column(name="id")
            table = Table(name="mydb.mytable", instance="postgres://db.host:5432")

            old_hwm = ColumnHWM(column=column, source=table, value=val)

            assert old_hwm.name == "id"
        """

        return self.column.name

    def __str__(self) -> str:
        """
        Returns full HWM name
        """

        return f"{self.name}#{self.source.full_name}"

    @property
    def qualified_name(self) -> str:
        """
        Unique name of HWM

        Returns
        -------
        value : str

            Qualified name

        Examples
        --------

        .. code:: python

            column = Column(name="id")
            table = Table(name="mydb.mytable", instance="postgres://db.host:5432")

            old_hwm = ColumnHWM(column=column, source=table, value=1)

            assert (
                old_hwm.qualified_name
                == "id#mydb.mytable@postgres://db.host:5432#currentprocess@currenthost"
            )
        """

        return "#".join([self.column.qualified_name, self.source.qualified_name, self.process.qualified_name])

    def covers(self, value: ColumnValueType) -> bool:
        """Return ``True`` if input value is already covered by HWM

        Examples
        --------

        .. code:: python

            column = Column(name="id")
            table = Table(name="mydb.mytable", instance="postgres://db.host:5432")

            old_hwm = ColumnHWM(column=column, source=table, value=1)

            assert old_hwm.covers(0)  # 0 <= 1
            assert old_hwm.covers(1)  # 1 <= 1
            assert old_hwm.covers(0.5)  # 0.5 <= 1
            assert not old_hwm.covers(2)  # 2 > 1

            empty_hwm = ColumnHWM(column=column, source=table)

            assert not empty_hwm.covers(0)  # non comparable with None
            assert not empty_hwm.covers(1)  # non comparable with None
            assert not empty_hwm.covers(0.5)  # non comparable with None
            assert not empty_hwm.covers(2)  # non comparable with None
        """

        if self.value is None:
            return False

        return self._check_new_value(value) <= self.value

    def update(self, value: ColumnValueType):
        """Updates current HWM value with some implementation-specific logic, and return HWM.

        .. note::

            Changes HWM value in place

        Returns
        -------
        result : ColumnHWM

            HWM copy with new value

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import IntHWM

            old_hwm = IntHWM(value=1, ...)

            old_hwm.update(2)
            assert old_hwm.value == 2

            old_hwm.update(1)
            assert old_hwm.value == 2  # value cannot decrease
        """

        if self.value is None:
            return self.set_value(value)

        if self.value < value:  # type: ignore[operator]
            return self.set_value(value)

        return self

    def __bool__(self):
        """Check if HWM value is set

        Returns
        -------
        result : bool

            ``False`` if ``value`` is ``None``, ``True`` otherwise

        Examples
        --------

        .. code:: python

            from etl_entities.old_hwm import ColumnHWM

            old_hwm = ColumnHWM(value=1, ...)
            assert old_hwm  # same as old_hwm.value is not None

            old_hwm = ColumnHWM(value=None, ...)
            assert not old_hwm
        """

        return self.value is not None

    def __add__(self, value):
        """Increase HWM value and return copy of HWM

        Parameters
        ----------
        value : ``Any`` or ``None``

            Should be compatible with ``value`` attribute type.

            For example, you cannot add ``str`` to ``int`` value, but you can add ``int`` to ``int``.

        Returns
        -------
        result : ColumnHWM

            HWM copy with new value

        Examples
        --------

        .. code:: python

            # assume val2 == val1 + inc

            hwm1 = ColumnHWM(value=val1, ...)
            hwm2 = ColumnHWM(value=val2, ...)

            # same as ColumnHWM(value=hwm1.value + inc, ...)
            assert hwm1 + inc == hwm2
        """

        new_value = self.value + value
        if self.value != new_value:
            return self.copy().set_value(new_value)

        return self

    def __sub__(self, value):
        """Decrease HWM value, and return copy of HWM

        Parameters
        ----------
        value : ``Any`` or ``None``

            Should be compatible with ``value`` attribute type.

            For example, you cannot subtract ``str`` from ``int`` value, but you can subtract ``int`` from ``int``.

        Returns
        -------
        result : ColumnHWM

            HWM copy with new value

        Examples
        --------

        .. code:: python

            # assume val2 == val1 - dec

            hwm1 = ColumnHWM(value=val1, ...)
            hwm2 = ColumnHWM(value=val2, ...)

            # same as ColumnHWM(value=hwm1.value - dec, ...)
            assert hwm1 - dec == hwm2
        """

        new_value = self.value - value
        if self.value != new_value:
            return self.copy().set_value(new_value)

        return self

    def __eq__(self, other):
        """Checks equality of two HWM instances

        Parameters
        ----------
        other : :obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` or any :obj:`object`

            You can compare two :obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` instances,
            obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` with an :obj:`object`,
            if its value is comparable with the ``value`` attribute of HWM

        Returns
        -------
        result : bool

            ``True`` if both inputs are the same, ``False`` otherwise.
        """

        if isinstance(other, HWM):
            self_fields = self.dict(exclude={"modified_time"})
            other_fields = other.dict(exclude={"modified_time"})
            return isinstance(other, ColumnHWM) and self_fields == other_fields

        return self.value == other

    def __lt__(self, other):
        """Checks current HWM value is less than another one

        Parameters
        ----------
        other : :obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` or any :obj:`object`

            You can compare two :obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` instances,
            obj:`etl_entities.old_hwm.column_hwm.ColumnHWM` with an :obj:`object`,
            if its value is comparable with the ``value`` attribute of HWM

            .. warning::

                You cannot compare HWMs if one of them has None value

        Returns
        -------
        result : bool

            ``True`` if current HWM value is less than provided value, ``False`` otherwise.
        """

        if isinstance(other, HWM):
            if isinstance(other, ColumnHWM):
                self_fields = self.dict(exclude={"value", "modified_time"})
                other_fields = other.dict(exclude={"value", "modified_time"})
                if self_fields == other_fields:
                    return self.value < other.value

                raise NotImplementedError(  # NOSONAR
                    "Cannot compare ColumnHWM with different column, source or process",
                )

            return NotImplemented

        return self.value < other
