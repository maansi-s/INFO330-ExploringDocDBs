from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['imported_pokemon_data']

# QUERY 3 - Write a query that returns all the Pokemon with an ability of "Overgrow"
pikachus = pokemonColl.find({'abilities': {"$regex": "Overgrow"}})
for row in pikachus:
    print(row)