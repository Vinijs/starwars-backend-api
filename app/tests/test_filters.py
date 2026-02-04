from app.helpers.filters import filter_by_search

def test_filter_by_search_found():
    data = [
        {"title": "A New Hope"},
        {"title": "The Empire Strikes Back"}
    ]

    result = filter_by_search(data, "hope", field="title")

    assert len(result) == 1
    assert result[0]["title"] == "A New Hope"


def test_filter_by_search_not_found():
    data = [
        {"title": "A New Hope"}
    ]

    result = filter_by_search(data, "xyz", field="title")

    assert result == []
