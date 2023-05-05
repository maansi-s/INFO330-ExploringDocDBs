import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("Players:") ## CHANGED FORMATTING
    print("The amazing " + pokemon1['name'] + "...")
    print("and the legendary" + pokemon2['name'] + "!")
    print()

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat + "!") ## ADDED PUNCTUATION
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior!!!!") ## ADDED PUNCTUATION

    winner = random.randrange(2)
    print()
    if winner == 0: print("Battle results... " + pokemon1['name'] + "!") ## CHANGED FORMATTING
    if winner == 1: print("Battle results... " + pokemon2['name'] + "!") ## CHANGED FORMATTING

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
