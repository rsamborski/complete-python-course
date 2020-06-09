# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

json_data = []

with open("csv_file.txt", "r") as csv_file:
    for line in csv_file:
        club, city, country = line.strip().split(",")
        json_data.append({"club": club, "country": country, "city": city})

with open("json_file.txt", "w") as json_file:
    json.dump(json_data, json_file)
