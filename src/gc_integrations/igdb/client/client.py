from gc_integrations.constants import IGDB_API_URL


class IGDBClient:
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token
        self.api_url = IGDB_API_URL
        
    