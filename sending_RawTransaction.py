from web3 import Web3

#I'm using ganache local network, for mainnet or testnets u can use Infuria (or any other node for your choice)
#https://web3py.readthedocs.io/en/stable/node.html
node_link = "http://127.0.0.1:7545" 
w3 = Web3(Web3.HTTPProvider(node_link))


account_1 = "0x53a0cB36AfCEBE9BB3490d62ED64D3469b8C1199"
privat_key = "84e990e4d0191d92c08321e00a3f8552f35cfc1da190fa648d95254306739485"
account_2 = "0xBaD047057a343B0dB3C065D5B1E67775f993D174"

nonce = w3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': Web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': Web3.toWei('50', 'gwei')
}

signed_tx = w3.eth.account.sign_transaction(tx, privat_key)
w3.eth.send_raw_transaction(signed_tx.rawTransaction)
