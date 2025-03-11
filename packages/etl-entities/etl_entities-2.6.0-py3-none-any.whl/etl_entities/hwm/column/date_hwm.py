# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import date
from typing import Optional

try:
    from pydantic.v1 import validator
    from pydantic.v1.validators import strict_str_validator
except (ImportError, AttributeError):
    from pydantic import validator  # type: ignore[no-redef, assignment]
    from pydantic.validators import strict_str_validator  # type: ignore[no-redef, assignment]

from etl_entities.hwm.column.column_hwm import ColumnHWM
from etl_entities.hwm.hwm_type_registry import register_hwm_type


@register_hwm_type("column_date")
class ColumnDateHWM(ColumnHWM[date]):
    """HWM based on tracking latest column value of type :obj:`datetime.date`.

    Parameters
    ----------
    name : ``str``

        HWM unique name

    value : :obj:`datetime.date` or ``None``, default: ``None``

        HWM value

    description : ``str``, default: ``""``

        Description of HWM

    source : Any, default: ``None``

        HWM source, e.g. table name

    expression : Any, default: ``None``

        Expression used to generate HWM value, e.g. ``column``, ``CAST(column as TYPE)``

    modified_time : :obj:`datetime.datetime`, default: current datetime

        HWM value modification time

    Examples
    --------

    .. code:: python

        from datetime import date
        from etl_entities.hwm import ColumnDateHWM

        hwm = ColumnDateHWM(
            name="long_unique_name",
            source="myschema.mytable",
            expression="my_date_column",
            value=date(year=2021, month=12, day=3),
        )
    """

    value: Optional[date] = None

    @validator("value", pre=True)
    def _validate_value(cls, value):  # noqa: N805
        # we need to deserialize values, as pydantic parses fields in unexpected way:
        # https://docs.pydantic.dev/latest/api/standard_library_types/#datetimedatetime
        if isinstance(value, int):
            raise ValueError("Cannot convert integer to date")

        if isinstance(value, str):
            result = strict_str_validator(value).strip()
            if result.lower() == "null":
                return None
            return date.fromisoformat(result)

        return value
