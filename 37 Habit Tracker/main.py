import requests
import datetime as dt

USERNAME = "pasan"
TOKEN = "jyg76TGUiouY&*TYYvrrhgJKGH"
GRAPH_ID = "graph1"

# create a new user.
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "jyg76TGUiouY&*TYYvrrhgJKGH",
    "username": "pasan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# create a new graph.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "my jogging graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# add a new pixel to the graph.
today = dt.datetime.now()
today = today.strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today,
    "quantity": input("How many kilometers did you walk today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


# update a pixel.
# update_pixel_config = {
#     "quantity": "7.18"
# }

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)


# delete a pixel.
# yesterday = dt.datetime(year=2022, month=6, day=14)
# yesterday= yesterday.strftime("%Y%m%d")

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)