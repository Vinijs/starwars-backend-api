from app.services.planets_service import (
    get_planets,
    search_planets,
    order_planets
)

def list_planets(search=None, page=None, order=None):
    if search:
        data = search_planets(search, page)
    else:
        data = get_planets(page)

    results = data.get("results", [])

    if order:
        results = order_planets(results, order)
        data["results"] = results

    return data
