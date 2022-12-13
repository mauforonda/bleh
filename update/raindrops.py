#!/usr/bin/env python3

import requests
import json
import os

TOKEN = os.getenv("RAINDROP_TOKEN")
FILENAME = 'data/raindrops.json'

def get_raindrops(search, perpage=50, sort="-created"):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"https://api.raindrop.io/rest/v1/raindrops/0?search={search}&perpage={perpage}&sort={sort}"
    response = requests.get(url, headers=headers)
    return response

def format_raindrops(response):
    data = [
        {
            field: item[field] for field in ["link", "title"]
        }
        for item in response.json()["items"]
    ]
    return data

def save_raindrops(data, filename):
    with open(filename, 'w+') as f:
        json.dump(data, f, ensure_ascii=False)

response = get_raindrops("type:article type:link match:OR", 20)
if response.status_code == 200:
    data = format_raindrops(response)
    save_raindrops(data, FILENAME)
