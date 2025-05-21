import os
import sqlite3
from flask import Flask, jsonify, render_template
from bokeh.plotting import figure
from bokeh.embed import json_item, components
from bokeh.resources import CDN
from jinja2 import Template


from bokeh.models import FactorRange

app = Flask(__name__)

page = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
  {{ resources }}
</head>
<body>
<h1>Cycle Data</h1>
  <div id="line_chart"></div>
<script>
  fetch('/line_chart')
      .then(function(response) { return response.json(); })
      .then(function(item) { 
          console.log("Bokeh item:", item); // Debugging: Log the item
          Bokeh.embed.embed_item(item, "line_chart"); 
      });
</script>
</body>
</html>
""")

def fetch_data():
    
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Execute a query to fetch the data
    cursor.execute("SELECT cd, temperature FROM data")
    rows = cursor.fetchall()
    conn.close()
    cycle_days = [row[0] for row in rows]
    temperatures = [row[1] for row in rows]


        # Debugging: Print the data
    print("Dates:", cycle_days)
    print("Temperatures:", temperatures)

    return cycle_days, temperatures


#create the line chart
def make_line_chart(cycle_days, temperatures):
    p = figure(
        title="Cycle Data", 
        x_axis_label='Cycle Day', 
        y_axis_label='Temperature',
        x_range=FactorRange(factors=cycle_days),
        sizing_mode="fixed", 
        width=600, 
        height=400)
    
    
    
    p.line(cycle_days, temperatures, legend_label="Temperature", line_width=2, color="blue")


    return p

#flask route to render line chart
@app.route('/')
def root():
    return page.render(resources=CDN.render())

@app.route('/line_chart')
def line_chart():
    cycle_days, temperatures = fetch_data()
    p = make_line_chart(cycle_days, temperatures)
    return jsonify(json_item(p, "line_chart"))

if __name__ == "__main__":
    app.run()