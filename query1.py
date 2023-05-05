import sqlite3
import sys
import json
import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['imported_pokemon_data']

# QUERY 1 - Write a query that returns all the Pokemon named "Pikachu"
pikachus = pokemonColl.find({'name': "Pikachu"})
for row in pikachus:
    print(row)
