from flask import Flask, jsonify, request
from app.services.swapi_service import get_swapi_resource
from app.helpers.filters import filter_by_search
from app.helpers.people_helper import list_people
from app.helpers.planets_helper import list_planets
from app.helpers.starships_helper import list_starships
from app.helpers.auth import token_required

API_KEY = "powerofdata123"

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
@token_required
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

@app.route("/planets")
@token_required
def planets():
    search = request.args.get("search")
    page = request.args.get("page")
    order = request.args.get("order")

    data = list_planets(
        search=search,
        page=page,
        order=order
    )
        
    
    return jsonify(data)

@app.route("/starships")
@token_required
def starships():
    search = request.args.get("search")
    page = request.args.get("page")
    order = request.args.get("order")

    data = list_starships(
        search=search,
        page=page,
        order=order
    )
        
    
    return jsonify(data)

def app_entry_point(request):
    return app

