import requests


headers = {"Content-Type": "application/json", "Accept": "application/json"}

data = {"IDNo":"IDNo0"}

response = requests.post("http://localhost:9090/blockchain/transaction/getTransactionByUserID", json = data, headers = headers)

print response.content