import requests

BASE_URL = "https://swapi.dev/api"

def get_swapi_resource(resource):
    response = requests.get(f"{BASE_URL}/{resource}/")
    response.raise_for_status()
    return response.json().get("results", [])