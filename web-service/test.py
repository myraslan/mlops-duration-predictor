import requests

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

url = 'http://localhost:5000/predict'
response = requests.post(url, json=ride)

print(response.json())