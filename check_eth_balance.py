from web3 import Web3

BASE_RPC = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(BASE_RPC))

# Example address (replace with any Base-compatible address)
address = "0x0000000000000000000000000000000000000000"

balance_wei = w3.eth.get_balance(address)
balance_eth = w3.from_wei(balance_wei, "ether")

print(f"ETH balance for {address}: {balance_eth} ETH")
