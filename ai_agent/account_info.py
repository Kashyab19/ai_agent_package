from .base import BlockchainAction
from pydantic import BaseModel
from typing import Dict, Any

class AccountRequest(BaseModel):
    """
    Schema for validating account fetch requests.
    """
    account_id: str  # e.g., "nearkat.testnet"

class AccountInfoFetcher(BlockchainAction):
    """
    Fetches account details from the NEAR blockchain.
    """

    def get_account_info(self, request: AccountRequest) -> Dict[str, Any]:
        """
        Fetches account information from NEAR.

        :param request: AccountRequest containing the account_id.
        :return: Account details in JSON format.
        """
        params = {
            "request_type": "view_account",  
            "finality": "final",
            "account_id": request.account_id,
        }

        return self.fetch_data("query", params)
