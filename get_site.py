import json

with open("top_sites.json", "r") as file:
    jsonified = file.read()
    datas = json.loads(jsonified)

index_list = []
sites = []
for country in datas:
    indexes = []
    data = country["data"]
    for i in range(50):
        site = data["Site"][i]
        contains = sum([site == _site for _site in sites])
        if not contains:
            indexes.append(i)
            sites.append(site)
    index_list.append(indexes)

cols = list(datas[0]["data"].keys())
site_data = {col: [] for col in cols}
for country_index in range(len(index_list)):
    country = datas[country_index]
    data = country["data"]
    for site_index in range(50):
        if site_index in index_list[country_index]:
            for col in cols:
                val = data[col][site_index]
                site_data[col].append(val)

with open("site_data.json", "w") as file:
    jsonified = json.dumps(site_data, indent=4)
    file.write(jsonified)

