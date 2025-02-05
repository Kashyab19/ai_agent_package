from typing import Any, Dict
import requests
import shutil
import subprocess

class BlockchainAction:
    """
    Base class for interacting with blockchain nodes.
    """

    RPC_URL = "https://rpc.testnet.near.org"

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
        
        
    @staticmethod
    def check_n_cli():
        """
        Check if the NEAR CLI is installed and available in the system's PATH.

        :raises EnvironmentError: If the NEAR CLI is not installed.
        """
        if not shutil.which("near"):
            raise EnvironmentError(
                "NEAR CLI is not installed. Please install it and try again."
            )

    @staticmethod
    def run_cli_command(command: list[str]) -> str:
        """
        Runs a NEAR CLI command and captures the output.

        :param command: List of command-line arguments for the NEAR CLI.
        :return: Output from the CLI command as a string.
        :raises RuntimeError: If the CLI command fails.
        """
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Error running NEAR CLI command: {' '.join(command)}\n{e.stderr}"
            )
