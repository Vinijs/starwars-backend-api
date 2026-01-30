from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API Star Wars rodando 🚀"
    })

@app.route("/films")
def get_films():
    return jsonify([
        {"id": 1, "title": "A New Hope", "year": 1977},
        {"id": 2, "title": "The Empire Strikes Back", "year": 1980},
        {"id": 3, "title": "Return of the Jedi", "year": 1983}
    ])

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

