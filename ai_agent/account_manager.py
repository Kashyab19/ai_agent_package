from .base import BlockchainAction
from pydantic import BaseModel
from typing import Dict, Any
import subprocess


class CreateAccountRequest(BaseModel):
    """
    Schema for validating NEAR account creation requests.
    """
    account_name: str


class AccountCreator(BlockchainAction):
    """
    Creates a new NEAR testnet account.
    """

    def create_account(self, request: CreateAccountRequest) -> Dict[str, Any]:
        """
        Creates a NEAR testnet account.

        :param request: CreateAccountRequest containing the account_name.
        :return: A dictionary with the account creation result.
        """
        self.check_n_cli()  # Ensure the NEAR CLI is installed and available.
        command = [
            "near",
            "create-account",
            request.account_name,
            "--useFaucet",
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {
                "status": "success",
                "message": f"Account '{request.account_name}' created successfully.",
                "details": result.stdout,
            }
        except subprocess.CalledProcessError as e:
            raise RuntimeError({
                "status": "error",
                "message": f"Error creating account '{request.account_name}'.",
                "details": e.stderr,
            })