from app.services.starships_service import (
    get_starships,
    search_starships,
    order_starships
)

def list_starships(search=None, page=None, order=None):
    if search:
        data = search_starships(search, page)
    else:
        data = get_starships(page)

    results = data.get("results", [])

    if order:
        results = order_starships(results, order)
        data["results"] = results

    return data
