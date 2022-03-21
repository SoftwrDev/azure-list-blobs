import os
import json
from datetime import datetime


def main():
    result = os.popen("az storage account list --query '[].{name:name}'").read()
    accounts = json.loads(result)

    for index, account in enumerate(accounts):
        print(f"{index+1}: {account['name']}")
    
    account_number = int(input("Account number: "))
    account_name = accounts[account_number - 1]["name"]
    
    connection_string = os.popen(f"az storage account show-connection-string -n {account_name}").read()

    container_name = input("Container name: ")
    result = os.popen(f"az storage blob list --container-name {container_name} --connection-string '{connection_string}'").read()

    today = datetime.now().strftime("%Y-%d-%m_%H-%M-%S")

    with open(f"tmp_{today}.json", "w") as f:
        f.write(json.dumps(json.loads(result), indent=4, sort_keys=False))

    print(f"Output writen to: tmp_{today}.json")

if __name__ == "__main__":
    main()
