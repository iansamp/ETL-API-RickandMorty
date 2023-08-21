# Extract

import requests
import pandas as pd
import csv


api_url = "https://rickandmortyapi.com/api/episode"

response = requests.get(api_url)
data = response.json()

episodes = data["results"]

print("Dados extraídos:")
print(episodes)

# Transform

total_episodes = len(episodes)

print("Número total de episódios:", total_episodes)

# Load

csv_filename = "episodes_data.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["id", "name", "air_date", "episode", "characters", "url", "created"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()

    for episode in episodes:
        writer.writerow(episode)
    
print("Dados carregados no arquivo CSV:", csv_filename)
