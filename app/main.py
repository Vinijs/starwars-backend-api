from flask import Flask, jsonify, request
from app.services.swapi_service import get_swapi_resource
from app.helpers.filters import filter_by_search
from app.helpers.people_helper import list_people

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API Star Wars rodando 🚀"
    })

@app.route("/films")
def get_films():
    search = request.args.get("search")
    films = get_swapi_resource("films")

    filtered = filter_by_search(films, search, field="title")

    if search and not filtered:
        return jsonify({"message" : "Filme não encontrado"}), 404
    
    return jsonify(filtered)

@app.route("/people")
def people():
    search = request.args.get("search")
    page = request.args.get("page")
    order = request.args.get("order")

    data = list_people(
        search=search,
        page=page,
        order=order
    )
        
    
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
