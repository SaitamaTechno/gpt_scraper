import requests
import json
from urllib.parse import quote

def gpt_ask(sentence):
    base_url = "http://192.168.1.236:80/api"
    api_key = "saitamatechno"
    #sentence = "adın ne? nasılsın?"
    # Encode the sentence for URL
    encoded_sentence = quote(sentence)

    # Construct the full URL
    url = f"{base_url}?api_key={api_key}&msg={encoded_sentence}"

    # Send the request
    response = requests.get(url)

    # Load the JSON response and print the message
    response_dict = json.loads(response.text)
    return response_dict

# Example usage
#answer=gpt_ask("!start")

answer=gpt_ask("who is your owner")
print(answer["message"])
