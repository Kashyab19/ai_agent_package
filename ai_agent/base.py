from typing import Any, Dict
import requests

class BlockchainAction:
    """
    Base class for interacting with blockchain nodes.
    """

    RPC_URL = "https://1rpc.io/near" # Has a rate-limit for free versions

    def fetch_data(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sends a JSON-RPC request to the blockchain.

        :param method: The RPC method to call.
        :param params: The parameters for the RPC method.
        :return: JSON response.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": method,
            "params": params,
        }
        try:
            response = requests.post(self.RPC_URL, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching data: {e}")
