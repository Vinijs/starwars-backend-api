import requests

BASE_URL = "https://swapi.dev/api"

def get_films():
    response = requests.get(f"{BASE_URL}/films/")
    response.raise_for_status()
    return response.json()["results"]

def search_films(title):
    response = requests.get(
        f"{BASE_URL}/films/",
        params={"search": title}
    )
    response.raise_for_status()
    return response.json()["results"]