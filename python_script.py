import requests

# print requests library version
print(requests.__version__)

# getting Google homepage
response = requests.get('https://www.google.com')

# downloads the file and runs itself     referenced: Mokhtar Ebrahim https://likegeeks.com/downloading-files-using-python/
script = requests.get('https://raw.githubusercontent.com/alinnmartinez/CMPUT404-lab-1-virtualenv-curl/main/python_script.py')

open('./script_to_read.py', 'wb').write(script.content)

file = open('./script_to_read.py', 'r')
print(file.read())