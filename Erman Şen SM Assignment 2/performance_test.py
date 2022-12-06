import json
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dict = {}

for i in range(10):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://en.wikipedia.org/wiki/Software_metric")
    t = driver.execute_script("return window.performance.getEntries();")
    for n in range(10):
        dict[t[n]["name"]] = t[n]["duration"]
    driver.close()

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in dict.items():
        writer.writerow(row)

jsonfile = json.dumps(dict)
print(jsonfile)
