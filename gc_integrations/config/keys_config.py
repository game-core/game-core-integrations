from pydantic import BaseSettings, Field
from dotenv import load_dotenv


class GCISecrets(BaseSettings):
    """A class that loads the environment variables from a .env file."""

    IGDB_CLIENT_ID: str = Field(default=None)
    IGDB_CLIENT_SECRET: str = Field(default=None)


def load_env_secrets():
    """Helper function to optionally load the environment variables from a .env file."""
    load_dotenv()
    secrets = GCISecrets()
    return secrets
