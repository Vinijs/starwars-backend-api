import requests

BASE_URL = "https://swapi.dev/api"

def get_planets(page=None):
    params = {}
    if page:
        params["page"] = page

    response = requests.get(f"{BASE_URL}/planets/", params=params)
    response.raise_for_status()
    return response.json()

def search_planets(name, page=None):
    params = {"search": name}
    if page:
        params["page"] = page

    response = requests.get(f"{BASE_URL}/planets/", params=params)
    response.raise_for_status()
    return response.json()

def order_planets(results, field):
    try:
        return sorted(
            results,
            key=lambda x: x.get(field) or ""
        )
    except Exception:
        return results