import requests
import json
import random

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {
            "letterPattern":"^[a-z]{1,7}$",
            "partOfSpeech":"adjective",
            "random":"true"}


headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': <API KEY> # Enter your Api Key here
    }

response = requests.request("GET", url, headers=headers, params=querystring)

a = json.loads(response.text)

genres = ['Scifi', 'Fantasy', 'Mystery', 'Drama', 'Romance', 'Action', 'Adventure']

print('Prompt: ' + a['word'].capitalize() + '\nGenre: ' + random.choice(genres))
