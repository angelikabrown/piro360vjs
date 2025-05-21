
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
<h1>Cycle Data</h1>
<body>
  <div id="line_chart"></div>
  <script>
  fetch('/line_chart)
      .then(function(response) { return response.json(); })
      .then(function(item) { return Bokeh.embed.embed_item(item, "line_chart"); });
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


#create the line chart
def make_line_chart(dates, temperatures):
    p = figure(title="Cycle Data", x_axis_label='Date', y_axis_label='Temperature', sizing_mode="fixed", width=400, height=400)
    p.line(dates, temperatures, legend_label="Temperature", line_width=2)
    return p

#flask route to render line chart
@app.route('/line_chart')
def line_chart():
    dates, temperatures = fetch_data()
    p = make_line_chart(dates, temperatures)
    return json.dumps(json_item(p, "line_chart"))

if __name__ == "__main__":
    app.run()