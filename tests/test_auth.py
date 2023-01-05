from unittest import IsolatedAsyncioTestCase

from gc_integrations.config.keys_config import load_env_secrets
from gc_integrations.igdb.models.auth_models import IGDBAuth
from gc_integrations.igdb.utils.utils import get_igdb_auth_token


class TestAuth(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.secrets = load_env_secrets()

    async def test_igdb_auth(self) -> None:
        auth = await get_igdb_auth_token(self.secrets.IGDB_CLIENT_ID, self.secrets.IGDB_CLIENT_SECRET)
        self.assertIsInstance(auth, IGDBAuth)
        self.assertIn("access_token", auth.dict().keys())
