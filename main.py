import pandas as pd
import json

with open("top_sites.json", "r") as file:
    jsonified = file.read()
    datas = json.loads(jsonified)

site_list = {country: {} for country in [x["name"] for x in datas]}

for country in datas:
    for i, site in enumerate(country["data"]["Site"]):
        site_list[country["name"]].update({i: site})

jsonified = json.dumps(site_list, indent=4)
with open("site_list.json", "w") as file:
    file.write(jsonified)

