from ai_agent.account_info import AccountInfoFetcher, AccountRequest

def test_account_info():
    agent = AccountInfoFetcher()
    request = AccountRequest(account_id="trywell.testnet")
    account_data = agent.get_account_info(request)

    # Print the response for debugging
    print("\nAccount Data Response:", account_data)

    # Ensure that we got a valid response
    
    assert "result" in account_data  # Ensure the "result" key exists
    
"""
curl -X POST https://1rpc.io/near \
     -H "Content-Type: application/json" \
     -d '{
           "jsonrpc": "2.0",
           "id": "dontcare",
           "method": "query",
           "params": {
             "request_type": "view_account",
             "finality": "final",
             "account_id": "root.near"
           }
         }'
"""
