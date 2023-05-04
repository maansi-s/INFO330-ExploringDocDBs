
##mongoimport --db=pokemondb --collection=pokemon_data --type=csv --fields "id,name,pokedex_number,types,hp,attack,defense,speed,sp_attack,sp_defense,abilities" --file=pokemon.csv

import sqlite3
import sys
import json
import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['imported_pokemon_data']

with open('pokemon.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    json_pokemon_data = []
    for row in reader:
        pokemon_data = {
            'name': row['name'],
            'pokedex_number': row['pokedex_number'],
            'types': '[' + row['type1'] + ', ' + row['type2'] + ']' if row['type2'] else '[' + row['type1'] + ']',
            'hp': row['hp'],
            'attack': row['attack'],
            'defense': row['defense'],
            'speed': row['speed'],
            'sp_attack': row['sp_attack'],
            'sp_defense': row['sp_defense'],
            'abilities': row['abilities']
        }
        json_pokemon_data.append(pokemon_data)

    pokemonColl.insert_many(json_pokemon_data)
    #pokemonColl.delete_many({})
    print("I found " + str(pokemonColl.count_documents({})) + " pokemon")

