import requests
response = requests.get("https://api.github.com/repos/LBK124/CV/compare/:base...:head")
print(response.json())
