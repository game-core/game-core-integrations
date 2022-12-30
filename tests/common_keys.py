import asyncio

from gc_integrations.config import load_env_secrets
from gc_integrations.igdb.utils import get_igdb_auth_token

igdb_secrets = load_env_secrets()
igdb_auth = None


async def load_common_secrets():
    global igdb_auth
    if igdb_auth is None:
        auth = await get_igdb_auth_token(igdb_secrets.IGDB_CLIENT_ID, igdb_secrets.IGDB_CLIENT_SECRET)
        igdb_auth = auth


asyncio.run(load_common_secrets())
