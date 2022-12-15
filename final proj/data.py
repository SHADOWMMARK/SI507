import csv
import requests
"""
    this py function runs as a result of saving a csv file as airports.csv
"""
# URL of the route data
url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"
urlP = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

# Get the data from the URL
response = requests.get(url)
responseP = requests.get(urlP)

# Write the data to a CSV file
csvfile =  open("routes.csv", "w", encoding="utf-8",newline="") 
writer = csv.writer(csvfile)
for line in response.text.splitlines():
    writer.writerow(line.split(",")[2:6])

csvfileP = open("airports.csv", "w", encoding="utf-8",newline="")
writer2 = csv.writer(csvfileP)
for line in responseP.text.splitlines():
    writer2.writerow(line.split(",")[4:8])
