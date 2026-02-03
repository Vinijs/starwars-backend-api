from app.services.people_service import (
    get_people,
    search_people,
    order_people
)

def list_people(search=None, page=None, order=None):
    if search:
        data = search_people(search, page)
    else:
        data = get_people(page)

    results = data.get("results", [])

    if order:
        results = order_people(results, order)
        data["results"] = results

    return data
