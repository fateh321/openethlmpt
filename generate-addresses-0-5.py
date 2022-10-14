#!/usr/bin/python3

import secrets
from eth_account import Account
# from eth_utils import privtoaddr
from web3 import Web3

num = 500000
FILE_NAME = "genesis_secrets_3.txt"
# Script to generate random secret keys
with open(FILE_NAME, "w") as f:
    for _ in range(num):
        s = str(secrets.token_hex(32))
        s1 = "0x" + s
        f.write(s1)
        f.write("\n")
    f.flush()
print(f"Secrets printed out in {FILE_NAME}")

# Script to generate a addr-balance mapping
genesis_secrets = f'"{FILE_NAME}"'
account_i = 0
balance_string = ""

for priv_key in open(genesis_secrets[1:-1], "r").readlines():
    priv_key = priv_key.strip()
    addr = Account.from_key(priv_key).address
    converted_addr = Web3.toChecksumAddress(addr)
    balance_string += f'"{converted_addr}": {{ "balance": "100000000000000000" }}'
    # print("\"%s\": { \"balance\": \"100000000000000000\"}," % converted_addr)
    account_i += 1
    if account_i == num:
        break
    else:
        balance_string += ",\n"

# Output addr-balance mapping
with open(FILE_NAME + ".json", "w") as f:
    output = f"{{\n{balance_string}\n}}"  # Format JSON here; can set to some template
    f.write(output)