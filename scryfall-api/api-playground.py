import requests
import json

def searchCard(card_name):
    url = "https://api.scryfall.com/cards/search"
    params = {
        'q': card_name
    }
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        filename = card_name + str(".json")
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

        print("Success")
        return None
    
    else:
        print(f"Error: {response.status_code}")
        return None
    
if __name__ == "__main__":
    card_name = "Black Lotus"
    card_data = searchCard(card_name)