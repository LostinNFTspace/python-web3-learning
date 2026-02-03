from web3 import Web3

BASE_RPC = "https://mainnet.base.org"

w3 = Web3(Web3.HTTPProvider(BASE_RPC))

if w3.is_connected():
    print("Connected to Base network")
    print("Chain ID:", w3.eth.chain_id)
else:
    print("Connection failed")
