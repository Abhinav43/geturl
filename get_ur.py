import requests
import os
import json
import time
import random

import giphy_client
from giphy_client.rest import ApiException

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
q = 'i work in a mechanic shop' # str | Search query term or prhase.
limit = 1 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)


def get_url(text):
    api_response = api_instance.gifs_search_get(api_key, text, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    all_gifs = []
    for per in api_response.to_dict()['data']:
        all_gifs.append(per['images']['downsized']['url'])
    return random.choice(all_gifs)
