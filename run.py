import requests

token = "c9f4bd850a7c8502dd5867967134bc916349025fd1a4a9ae5ced534df5376bb6"

headers = {
    "Authorization": "Bearer %s" % token,
}

response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)