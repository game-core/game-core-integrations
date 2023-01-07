from unittest import IsolatedAsyncioTestCase
from gc_integrations.hltb import HowLongToBeatClient


class TestHltb(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = HowLongToBeatClient()

    async def test_search(self) -> None:
        results = await self.client.search("Super Mario Odyssey")
        self.assertTrue(len(results) > 0)

    async def test_dlc_search(self) -> None:
        results = await self.client.search_DLCs("The Ringed City")
        self.assertTrue(len(results) > 0)
        
    
