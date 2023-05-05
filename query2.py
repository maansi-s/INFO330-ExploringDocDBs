import sqlite3
import sys
import json
import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['imported_pokemon_data']

# QUERY 2 - Write a query that returns all the Pokemon with an attack greater than 150
pikachus = pokemonColl.find({'attack': {'$gt': 150}})
for row in pikachus:
    print(row)
