# HTTPS Requests
# Get - requests.get() we make a request and get back a response
# Post - requests.post() we make a request but we are not very interested with the reponse
# Put - requests.put() we update a piece of data in an external service
# Delete - requests.delete() we delete a piece of data posted in an external service

import requests
from datetime import datetime

USERNAME = "nuray"
TOKEN = "PYTHONtest123"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# The username was creted once, no need to do it several times:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "BootcampTrackerGraph",
    "unit": "lesson",
    "type": "int",
    "color": "ichou",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# https://pixe.la/v1/users/nuray/graphs/graph1

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# if i want to get another day
# today = datetime(year=2021, month=8, day=21)

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Have you watched your lesson today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)

edit_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

edit_pixel_config = {
    "quantity": "1"
}

delete_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=delete_pixel_endpoint, json=edit_pixel_config, headers=headers)
# print(response.text)


# response = requests.delete(url=edit_pixel_endpoint, headers=headers)

