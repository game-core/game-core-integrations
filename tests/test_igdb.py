from unittest import IsolatedAsyncioTestCase

from tests.common_keys import igdb_auth, igdb_secrets
from gc_integrations.igdb import IGDBClient
from time import sleep


class TestIGDB(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.bearer_token = igdb_auth.access_token
        self.client_id = igdb_secrets.IGDB_CLIENT_ID
        self.client = IGDBClient(self.client_id, self.bearer_token)

    async def test_games(self):
        endpoint = "games"
        request = await self.client.make_request(endpoint)
        print(request)
        self.assertIsInstance(request, list)
        self.assertGreater(len(request), 0)

    async def test_games_with_query(self):
        endpoint = "games"
        query = {"fields": "name", "where": "name = \"Super Mario 64\";"}
        request = await self.client.make_request(endpoint, query)
        print(request)
        self.assertIsInstance(request, list)
        self.assertGreater(len(request), 0)

    async def test_similars_resolve(self):
        games_ids = [18115, 19222, 25905, 41349, 85804, 87170, 87507, 90788, 90965, 95776]
        request = await self.client.resolve_similars(games_ids)
        self.assertGreater(len(request), 0)
