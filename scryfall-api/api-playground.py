import requests
import json
import os
from time import sleep

def searchCard(card_name, set):
    url = "https://api.scryfall.com/cards/search"
    params = {
        'q': card_name + " set:" + set
    }
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        directory = "scryfall-api/json-files"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, card_name + ".json")

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

        print("Success")
    
    else:
        print(f"Error: {response.status_code}")

    sleep(0.1)
    
if __name__ == "__main__":
    card_name = "Ashling, Flame Dancer"
    card_set = "mh3"
    card_data = searchCard(card_name, card_set)