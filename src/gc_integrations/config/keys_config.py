from pydantic import BaseSettings, Field


class GCISecrets(BaseSettings):
    """A class that loads the environment variables from a .env file."""

    IGDB_CLIENT_ID: str = Field(default=None)
    IGDB_AUTH_TOKEN: str = Field(default=None)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def load_env_secrets():
    """Helper function to optionally load the environment variables from a .env file."""
    return GCISecrets()
