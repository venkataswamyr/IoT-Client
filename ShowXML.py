import requests
response = requests.get("https://openioe.herokuapp.com/Console/showxml/1143/215")
print response.text

