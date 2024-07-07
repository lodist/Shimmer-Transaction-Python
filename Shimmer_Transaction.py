import sys

def shimmer_transact(recipient_address):
    print('Start Shimmer transaction')
        
    from iota_sdk import (
        Client,
        CoinType,
        StrongholdSecretManager,
        Wallet,
        ClientOptions,
        SendNativeTokensParams,
    )
        
    import logging

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s: %(message)s')

    # Configuration parameters
    node_url = "https://api.shimmer.network"
    account_alias = "MyAccountAlias"
    stronghold_path = "/path/to/your/wallet.stronghold"
    stronghold_password = "your_stronghold_password"

    # Initialize Stronghold secret manager
    secret_manager = StrongholdSecretManager(stronghold_path, stronghold_password)

    # Create ClientOptions instance
    client_options = ClientOptions(nodes=[node_url])

    # Initialize the Wallet instance
    wallet = Wallet(
        client_options=client_options,
        coin_type=CoinType.SHIMMER,
        secret_manager=secret_manager,
    )

    try:
        # Try to access the existing account
        account = wallet.get_account(account_alias)
        print(f"Accessed existing account with alias '{account_alias}'")
    except Exception as e:
        # If accessing the account fails, it likely doesn't exist, so create it
        print(f"Account '{account_alias}' not found. Creating a new account...")
        account = wallet.create_account(account_alias)
        print(f"New account created with alias '{account_alias}'")

    # Sync the account with the node
    account.sync()
    print(f"Account '{account_alias}' synced with the node.")

    # Check balance
    balance = account.get_balance()
    print("Balance object:", balance)

    # Check if there are any native tokens
    native_tokens_balances = balance.nativeTokens
    if native_tokens_balances:
        for token_balance in native_tokens_balances:
            # Converting from hexadecimal to integer for readable format
            total_tokens = int(token_balance.total, 16)
            print(f"Token ID: {token_balance.tokenId}, Total: {total_tokens}")
    else:
        print("No native tokens in the balance.")

    # Define the token ID and amount to be sent
    token_id = "0xYourTokenID"
    token_amount = 1  # The amount of native tokens to send

    # Set Stronghold password (ensure this is done securely)
    wallet.set_stronghold_password(stronghold_password)

    # Prepare native tokens for the transaction
    outputs = [SendNativeTokensParams(recipient_address, [(token_id, hex(token_amount))])]

    # Send native tokens
    transaction = account.send_native_tokens(outputs, None)
    print(f"Transaction sent: {transaction.transactionId}")

    # Wait for transaction to get included
    blockId = account.retry_transaction_until_included(transaction.transactionId)
    print(f"Block included: {blockId}")

    # Sync again to update the balance
    balance = account.sync()
    print(f"New Balance: {balance}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 shimmer_transact.py 'recipient_address'")
        sys.exit(1)
    
    recipient_address = sys.argv[1]
    shimmer_transact(recipient_address)
