from web3 import Web3

#I'm using ganache local network, for mainnet or testnets u can use Infuria (or any other node for uour choice)
#https://web3py.readthedocs.io/en/stable/node.html
node_link = "http://127.0.0.1:7545" 
w3 = Web3(Web3.HTTPProvider(node_link))


address = "0x53a0cB36AfCEBE9BB3490d62ED64D3469b8C1199"
print(Web3.fromWei(w3.eth.get_balance(address), "ether"))
