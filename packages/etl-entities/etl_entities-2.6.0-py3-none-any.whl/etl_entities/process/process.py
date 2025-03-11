# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import logging
import os
import re
from socket import getfqdn

import psutil
import typing_extensions

try:
    from pydantic.v1 import ConstrainedStr, Field, validator
except (ImportError, AttributeError):
    from pydantic import ConstrainedStr, Field, validator  # type: ignore[no-redef, assignment]

from etl_entities.entity import BaseModel, Entity
from etl_entities.instance import Host

log = logging.getLogger(__name__)


# dag or task name cannot have delimiters used in qualified_name
class DagTaskName(ConstrainedStr):
    regex = re.compile("^[^.]*$")


@typing_extensions.deprecated(
    "Deprecated in v2.0, will be removed in v3.0",
    category=UserWarning,
)
class Process(BaseModel, Entity):
    """Process representation

    .. deprecated:: 2.0.0

    Parameters
    ----------
    name : :obj:`str`, default: current process name

        Process name

    host : :obj:`str`, default: current host FQDN

        Host name. Could be hostname, FQDN or IPv4/IPv6 address

    task : :obj:`str`, default: empty string

        Task name

        .. warning::

            Can be set only if ``dag`` set too

    dag : :obj:`str`, default: empty string

        DAG name

        .. warning::

            Can be set only if ``task`` is set too

    Examples
    --------

    .. code:: python

        from etl_entities import Process

        process = Process()
        process1 = Process(name="myprocess")
        process2 = Process(name="myprocess", host="myhost")
        process3 = Process(name="myprocess", task="abc", dag="cde", host="myhost")
    """

    name: str = Field(default_factory=lambda: psutil.Process(os.getpid()).name())
    host: Host = Field(default_factory=getfqdn)  # type: ignore[assignment]
    dag: DagTaskName = DagTaskName()
    task: DagTaskName = DagTaskName()

    @validator("task", always=True)
    def task_and_dag_should_be_both_set(cls, task, values):  # noqa: N805
        dag = values.get("dag")

        if bool(task) ^ bool(dag):
            raise ValueError("task and dag should be both set or both empty")

        return task

    @property
    def full_name(self) -> str:
        """
        Full process name

        Returns
        -------
        value : str

            Process full name

        Examples
        --------

        .. code:: python

            from etl_entities import Process

            process1 = Process(name="myprocess")
            process2 = Process(name="myprocess", task="abc", dag="cde")

            assert process1.full_name == "myprocess"
            assert process2.full_name == "cde.abc.myprocess"
        """

        return ".".join(filter(None, (self.dag, self.task, self.name)))

    def __str__(self):
        """
        Returns full process name
        """

        return self.full_name

    @property
    def qualified_name(self) -> str:
        """
        Unique name of process

        Returns
        -------
        value : str

            Qualified name

        Examples
        --------

        .. code:: python

            from etl_entities import Process

            process1 = Process(name="myprocess", host="myhost")
            assert process1.qualified_name == "currentapp@somehost"

            process2 = Process(name="myprocess", task="abc", dag="cde", host="myhost")
            assert process2.qualified_name == "abc.cde.currentapp@somehost"
        """

        return "@".join([self.full_name, self.host])

    def __enter__(self):
        """
        Enter the process context

        Examples
        --------

        .. code:: python

            from etl_entities import Process

            with Process(name="myprocess", host="myhost") as process:
                ...
        """

        # hack to avoid circular imports
        from etl_entities.process.process_stack_manager import ProcessStackManager

        log.debug(f"{self.__class__.__name__}: Entered stack at level {ProcessStackManager.get_current_level()}")
        ProcessStackManager.push(self)
        log.info(f"{self.__class__.__name__}: Using process {self}")
        return self

    def __exit__(self, exc_type, _exc_value, _traceback):
        from etl_entities.process.process_stack_manager import ProcessStackManager

        log.debug(f"{self.__class__.__name__}: Exiting stack at level {ProcessStackManager.get_current_level() - 1}")
        ProcessStackManager.pop()
        return False
