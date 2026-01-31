from flask import Flask, jsonify, request
from app.services.swapi_service import get_films, search_films

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
