from typing import Self
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Product


class MongoDB(object):

    def __init__(self):
        self._client = self.create_client()
        self._db = self._client['wb_database']

    async def __aenter__(self) -> Self:
        if self._client is None:
            raise Exception("Databased connector is not initialized")

        await init_beanie(database=self._db, document_models=[Product])
        return self

    async def __aexit__(self, type, value, traceback):
        self._client.close()

    @staticmethod
    def create_client():
        """
        Creates client for docker-compose container
        """
        uri = "dkrcomp-mongo"
        client = AsyncIOMotorClient(uri)
        return client
