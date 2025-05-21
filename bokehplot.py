
import json
import sqlite3
from flask import Flask
from jinja2 import Template

from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.sampledata.penguins import data

app = Flask(__name__)

page = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
  {{ resources }}
</head>
<h1>Penguin size</h1>
<body>
  <div id="myplot"></div>
  <div id="myplot2"></div>
  <script>
  fetch('/plot')
    .then(function(response) { return response.json(); })
    .then(function(item) { return Bokeh.embed.embed_item(item); })
  </script>
  <script>
  fetch('/plot2')
    .then(function(response) { return response.json(); })
    .then(function(item) { return Bokeh.embed.embed_item(item, "myplot2"); })
  </script>
</body>
""")

def fetch_data():
    conn = sqlite3.connect('cyclesync.db')
    cursor = conn.cursor()

    # Execute a query to fetch the data
    cursor.execute("SELECT date, temperature FROM Data")
    rows = cursor.fetchall()
    conn.close()
    dates = [row[0] for row in rows]
    temperatures = [row[1] for row in rows]
    return dates, temperatures
