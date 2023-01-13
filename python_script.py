import requests

# print requests library version
print(requests.__version__)

# getting Google homepage
response = requests.get('https://www.google.com')