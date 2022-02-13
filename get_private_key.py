from web3.auto import w3
import binascii
with open("~/.ethereum/keystore/UTC--2018-06-10T05-43-22.134895238Z--6318670a866a260e9a26eee1eb40ba98fdc0ba0e") as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key,'password')
        print(binascii.b2a_hex(private_key))


