import sqlite3
import sys
import json
import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['imported_pokemon_data']

connection = sqlite3.connect('/Users/maansisurve/Desktop/INFO330/INFO330-ExploringDocDBs/pokemon.sqlite')
table = connection.cursor()

# QUERY 1 - Write a query that returns all the Pokemon named "Pikachu"
table.execute('SELECT * FROM imported_pokemon_data WHERE name = "Pikachu"')
for row in table:
    print(row)

# QUERY 2 - Write a query that returns all the Pokemon with an attack greater than 150
table.execute('SELECT * FROM imported_pokemon_data WHERE attack > 150')
for row in table:
    print(row)

# QUERY 3 - Write a query that returns all the Pokemon with an ability of "Overgrow"