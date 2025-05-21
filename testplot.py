from bokeh.plotting import figure
from bokeh.embed import json_item
import json

# Create a simple plot
p = figure(
    title="Test Plot",
    x_axis_label='X',
    y_axis_label='Y')
p.line([1, 2, 3], [4, 5, 6])

# Generate the JSON item
bokeh_json = json_item(p, "test_div")

# Print the JSON to inspect it
print(json.dumps(bokeh_json, indent=2))