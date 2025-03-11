# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import re
from typing import OrderedDict

import typing_extensions

try:
    from pydantic.v1 import ConstrainedStr, Field, validator
except (ImportError, AttributeError):
    from pydantic import ConstrainedStr, Field, validator  # type: ignore[no-redef, assignment]

from etl_entities.entity import BaseModel, Entity


# column or partition name cannot have delimiters used in qualified_name
class ColumnName(ConstrainedStr):
    regex = re.compile(r"^[^\|/=@#]+$")


@typing_extensions.deprecated(
    "Deprecated in v2.0, will be removed in v3.0",
    category=UserWarning,
)
class Column(BaseModel, Entity):
    """DB column representation

    .. deprecated:: 2.0.0

    Parameters
    ----------
    name : str

        Table name

        .. warning::

            Cannot contain symbols ``|``, ``/``, ``=``, ``@`` and ``#``

    partition : :obj:`collections.OrderedDict`, default: empty dict

        Partition which column belong to, e.g. ``partcolumn=value1/partcolumn2=value2``

        .. warning::

            Names and values cannot contain symbols ``|``, ``/``, ``=``, ``@`` and ``#``

    Examples
    --------

    .. code:: python

        from etl_entities import Column

        column1 = Column(name="mycolumn")
        column2 = Column(
            name="mycolumn", partition={"partcolumn": "value1", "partcolumn2": "value2"}
        )
    """

    name: ColumnName
    partition: OrderedDict[ColumnName, ColumnName] = Field(default_factory=OrderedDict)

    def __str__(self):
        """
        Returns column name
        """

        return self.name

    @validator("partition", pre=True)
    def parse_partition_str(cls, value):  # noqa: N805
        if isinstance(value, str):
            value = value.strip()
            result = OrderedDict()
            for item in value.strip("/").split("/"):
                if item.count("=") != 1:
                    raise ValueError(f"Partition should be passed in format 'name=value', got '{item}'")

                key, value = item.split("=")
                if key in result:
                    raise ValueError(f"Passed multiple values for {key} partition column")

                result[key] = value

            return result

        return OrderedDict(value)

    @property
    def partition_kv(self) -> str:
        return "/".join(f"{k}={v}" for k, v in self.partition.items())

    @property
    def qualified_name(self) -> str:
        """
        Unique name of column

        Returns
        -------
        value : str

            Qualified name

        Examples
        --------

        .. code:: python

            from etl_entities import Table

            column1 = Column(name="mycolumn")
            column2 = Column(
                name="mycolumn", partition={"partcolumn": "value1", "partcolumn2": "value2"}
            )

            assert column1.qualified_name == "mycolumn"
            assert column2.qualified_name == "mycolumn|partcolumn1=value1/partcolumn2=value2"
        """

        if self.partition_kv:
            return f"{self}|{self.partition_kv}"

        return str(self)
