"""Vault secrets engines endpoints"""

import typing as tp

from vaultx import exceptions
from vaultx.adapters import Adapter
from vaultx.api.secrets_engines.kv import Kv
from vaultx.api.secrets_engines.kv_v1 import KvV1
from vaultx.api.secrets_engines.kv_v2 import KvV2
from vaultx.api.vault_api_base import VaultApiBase


__all__ = (
    "Kv",
    "KvV1",
    "KvV2",
    "SecretsEngines",
)


@exceptions.handle_unknown_exception
class SecretsEngines(VaultApiBase):
    """Secrets Engines."""

    _implemented_classes: tp.Final[dict] = {
        "_kv": Kv,
    }

    def __init__(self, adapter: Adapter) -> None:
        for attr_name, _class in self._implemented_classes.items():
            setattr(self, attr_name, _class(adapter=adapter))
        super().__init__(adapter)

    def __getattr__(self, item: str):
        """
        Get an instance of a class instance.

        :param item: Name of the class being requested.
        :return: The requested class instance where available.
        """
        item = f"_{item}"
        if item in self._implemented_classes:
            return getattr(self, item)
        raise AttributeError

    @property
    def adapter(self) -> Adapter:
        """
        Retrieve the adapter instance under the "_adapter" property in use by this class.

        :return: The adapter instance in use by this class.
        """
        return self._adapter

    @adapter.setter
    def adapter(self, adapter) -> None:
        """
        Set the adapter instance under the "_adapter" property in use by this class.
        Also set the adapter property for all implemented classes.

        :param adapter: New adapter instance to set for this class and all implemented classes.
        """
        self._adapter = adapter
        for implemented_class in self._implemented_classes:
            getattr(self, f"{implemented_class}").adapter = adapter
