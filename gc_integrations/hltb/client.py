from typing import Optional

from howlongtobeatpy import HowLongToBeat
from howlongtobeatpy.HTMLRequests import SearchModifiers

class HowLongToBeatClient:
    def __init__(self) -> None:
        self.client = HowLongToBeat()

    async def search(self, query: str, with_DLCs: Optional[bool] = True) -> dict:
        if with_DLCs:
            search_modifiers = SearchModifiers.NONE
        else:
            search_modifiers = SearchModifiers.HIDE_DLC
        results = self.client.search(query, search_modifiers)
        return results

    async def search_DLCs(self, query: str) -> dict:
        results = self.client.search(query, SearchModifiers.ISOLATE_DLC)
        return results



