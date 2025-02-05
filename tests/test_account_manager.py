from ai_agent.account_manager import AccountCreator, CreateAccountRequest
import shutil
import subprocess

def test_create_account():
    agent = AccountCreator()
    request = CreateAccountRequest(account_name="trywell.testnet")
    
    try:
        # Attempt to create the account
        account_creation_response = agent.create_account(request)
        
        # Print the response for debugging
        print("\nAccount Creation Response:", account_creation_response)
        
        # Ensure the response indicates success
        assert account_creation_response["status"] == "success"
        assert "message" in account_creation_response
        assert "details" in account_creation_response

    except RuntimeError as e:
        # If an error is raised, print it for debugging
        print("\nAccount Creation Error:", e)
        assert False, "Account creation failed unexpectedly."
