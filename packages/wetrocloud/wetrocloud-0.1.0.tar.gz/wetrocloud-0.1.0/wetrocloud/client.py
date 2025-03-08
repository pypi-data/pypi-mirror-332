import requests

class Wetrocloud:
    pass


class WetroRAG(Wetrocloud):
    def __init__(self, api_key: str):
        """
        Initialize the Wetrocloud API client.
        
        :param api_key: Your API key for authentication
        :param base_url: Base URL for the API (default is Wetrocloud's production URL)
        """
        self.api_key = api_key
        self.base_url = "https://api.wetrocloud.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.collection_id = None
        self.model = None

    def set_collection_id(self, collection_id: str):
        """
        creates or get collection id then sents it to self.collection_id
        """
        url = f"{self.base_url}/create/"
        payload = {
            "collection_id": collection_id
        }
        response = requests.post(url, headers=self.headers, payload=payload)
        return self._handle_response(response)
    
    def add_resource(self, resource: str, type:str):
        """
        """
        url = f"{self.base_url}/insert/"
        payload = {
            "collection_id": self.collection_id,
            "resource": resource,
            "type": type,
            "model": self.model
        }
        response = requests.post(url, headers=self.headers, payload=payload)

        return self._handle_response(response)
    
    def query(self, query: str, json_schema = None, rules = None ):
        """
        """
        url = f"{self.base_url}/query/"
        data = {
            "collection_id": self.collection_id,
            "request_query": query,
            "model": self.model
        }
        if self._validate_json_schema(json_schema,rules):
            data["json_schema"] = json_schema
            data["json_schema_rules"] = rules

        response = requests.post(url, headers=self.headers, json=data)

        return self._handle_response(response)
    
    def _validate_json_schema(self,json_schema,rules):
        """
        returns boolean
        """
        pass

    def _handle_response(self, response):
        """
        Handles API response, raising errors if necessary.
        """
        if response.status_code >= 400:
            raise Exception(f"Error {response.status_code}: {response.text}")
        return response.json()
