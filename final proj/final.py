from flask import Flask
import urllib.request
import csv
import collections

app = Flask(__name__)

def lauchData():
    sourceToDes = collections.defaultdict(list)
    with open("routes.csv","r") as f:
        reader = csv.reader(f)
        for line in reader:
            if line:
                sourceToDes[line[0]].append(line[2])
    return sourceToDes

@app.route('/')
def index():
    # Download the data from the website
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"
    with urllib.request.urlopen(url) as response:
       data = response.read()

    # Use the csv library to parse the data
    routes = csv.reader(data.decode('utf-8').splitlines(), delimiter=",")

    # Build a response string with the first few rows of the data
    response_str = "<h1>Routes Data</h1>"
    response_str += "<ul>"
    for route in routes:
        response_str += "<li>" + str(route) + "</li>"
    response_str += "</ul>"
    return response_str


if __name__ == "__main__":
    STODdata = lauchData()
    print(STODdata['AER'])
    # app.run()
