from web3 import Web3

BASE_RPC = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(BASE_RPC))

block_number = w3.eth.block_number
print("Latest Base block:", block_number)
