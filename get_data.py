from selenium import webdriver
import json
from tqdm import tqdm

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("https://www.alexa.com/topsites/countries")

country_elems = driver.find_elements_by_css_selector("div.categories.top > ul.countries > li > a")
country_names = [x.get_attribute("innerText") for x in country_elems]
country_links = [x.get_attribute("href") for x in country_elems]

data_list = []
for j in tqdm(range(len(country_links))):
    link = country_links[j]
    name = country_names[j]
    driver.get(link)
    table = driver.find_element_by_css_selector("div.listings.table")
    col_elems = table.find_elements_by_css_selector(".thead > .tr > .th")
    cols = [x.get_attribute("innerText") for x in col_elems[1:]]
    datas = {}
    data = {}
    for col in cols:
        data.update({col: []})
    row_elems = table.find_elements_by_css_selector(".tr.site-listing")
    for elem in row_elems:
        val_elems = elem.find_elements_by_css_selector(".td")
        vals = [x.get_attribute("innerText") for x in val_elems[1:]]
        for i in range(len(cols)):
            col = cols[i]
            val = vals[i]
            data[col].append(val)
    datas.update({"name": name, "link": link, "data": data})
    data_list.append(datas)
jsonified = json.dumps(data_list, indent=4)
with open("top_sites.json", "w") as file:
    file.write(jsonified)
