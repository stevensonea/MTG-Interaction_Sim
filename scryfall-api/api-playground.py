import requests
import json
import os
from time import sleep

def searchCard(cards):
    url = "https://api.scryfall.com/cards/search"

    for card in cards:
        params = {
            'q': card
        }
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            directory = "scryfall-api/json-files"
            if not os.path.exists(directory):
                os.makedirs(directory)

            filename = os.path.join(directory, card + ".json")

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            print("Success")
        
        else:
            print(f"Error: {response.status_code}")
        
        sleep(.1)
    
if __name__ == "__main__":
    cards = ["Black Lotus", "Ashling", "Sol Ring", "Sulfer"]
    card_data = searchCard(cards)