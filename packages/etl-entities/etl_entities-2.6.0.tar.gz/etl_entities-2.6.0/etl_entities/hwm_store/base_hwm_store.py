# SPDX-FileCopyrightText: 2021-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

from etl_entities.entity import BaseModel
from etl_entities.hwm import HWM

log = logging.getLogger(__name__)


class BaseHWMStore(BaseModel, ABC):
    def __enter__(self):
        """
        HWM store context manager.

        Enter this context to use this HWM store instance as current one (instead default).

        Examples
        --------

        >>> from etl_entities.hwm_store import HWMStoreStackManager
        >>> with SomeHWMStore(...) as hwm_store:
        ...     print(HWMStoreStackManager.get_current())
        SomeHWMStore(...)
        >>> HWMStoreStackManager.get_current()
        DefaultHWMStore()
        """
        # hack to avoid circular imports
        from etl_entities.hwm_store.hwm_store_stack_manager import HWMStoreStackManager

        log.debug("|%s| Entered stack at level %d", self.__class__.__name__, HWMStoreStackManager.get_current_level())
        HWMStoreStackManager.push(self)

        self._log_parameters()
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        from etl_entities.hwm_store.hwm_store_stack_manager import HWMStoreStackManager

        log.debug(
            "|%s| Exiting stack at level %d",
            self.__class__.__name__,
            HWMStoreStackManager.get_current_level() - 1,
        )
        HWMStoreStackManager.pop()
        return False

    @abstractmethod
    def get_hwm(self, name: str) -> HWM | None:
        """
        Get HWM by name from HWM store.

        Parameters
        ----------
        name : str
            HWM unique name

        Returns
        -------
        :obj:`HWM <etl_entities.hwm.HWM>`
            HWM object, if it exists in HWM store, or None

        Examples
        --------

        .. code:: python

            hwm = hwm_store.get_hwm(hwm_unique_name)
        """

    @abstractmethod
    def set_hwm(self, hwm: HWM) -> Any:
        """
        Save HWM object to HWM Store.

        Parameters
        ----------
        hwm : :obj:`HWM <etl_entities.hwm.HWM>`
            HWM object

        Returns
        -------
        Any
            HWM location, like URL of file path. Result type is implementation-specific.

        Examples
        --------

        .. code:: python

            from etl_entities.hwm import ColumnIntHWM

            hwm = ColumnIntHWM(name=..., value=...)
            hwm_location = hwm_store.set_hwm(hwm)
        """

    def _log_parameters(self) -> None:
        log.info("Using %s as HWM Store", self.__class__.__name__)
        options = self.dict(by_alias=True, exclude_none=True)

        if options:
            log.info("|%s| Using options:", self.__class__.__name__)
            for option, value in options.items():
                log.info("    %s = %r", option, value)
