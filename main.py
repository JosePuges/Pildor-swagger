from fastapi import FastAPI
import requests

app = FastAPI()

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


@app.get("/")
def home():
    return {"message": "API de Pokémon funcionando"}


@app.get("/pokemon")
def get_pokemon_list(limit: int = 5):
    response = requests.get(f"{BASE_URL}?limit={limit}")
    data = response.json()
    return data["results"]


@app.get("/pokemon/{name}")
def get_pokemon_by_name(name: str):
    response = requests.get(f"{BASE_URL}/{name.lower()}")

    if response.status_code != 200:
        return {"error": "Pokémon no encontrado"}

    data = response.json()

    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"]
    }

# Ejecutar uvicorn en la terminal con: 
# uvicorn main:app --reload