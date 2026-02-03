def filter_by_search(items, search, field="title"):
    if not search:
        return items
    
    search = search.lower()

    return [
        item for item in items
        if search in item.get(field, "").lower()
    ]