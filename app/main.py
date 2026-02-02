from flask import Flask, jsonify, request
from app.services.swapi_service import get_films, search_films
from app.services.people_service import get_people, search_people, order_people

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API Star Wars rodando 🚀"
    })

@app.route("/films")
def films():
    search = request.args.get("search")

    if search:
        results = search_films(search)
        if not results:
            return jsonify({"message": "No films found"}), 404
        return jsonify(results)
    
    return jsonify(get_films())

@app.route("/people")
def people():
    search = request.args.get("search")
    page = request.args.get("page")
    order = request.args.get("order")

    if search:
        data = search_people(search, page)
    else:
        data = get_people(page)

    results = data.get("results", [])

    if order:
        results = order_people(results, order)
        data["results"] = results
        
    
    return jsonify(data)

@app.route("/films/<int:film_id>")
def get_film_by_id(film_id):
    films_list = [
        {"id": 1, "title": "A New Hope", "year": 1977},
        {"id": 2, "title": "The Empire Strikes Back", "year": 1980},
        {"id": 3, "title": "Return of the Jedi", "year": 1983}
    ]

    for film in films_list:
        if film["id"] == film_id:
            return jsonify(film)

    return jsonify({"error": "Film not found"}), 404
