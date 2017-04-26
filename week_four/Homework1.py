# Bokeh -> Library for realy cool interactive (cybercyber) graphics in python e.g. tool to allow text to pop up on a plot when the cursor
# hovers over it.  Also, we import a data structure used to store arguments
# of what to plot in Bokeh

from bokeh.models import HoverTool, ColumnDataSource
import bokeh.io as bio
import bokeh.plotting.figure as bplot
import pandas as pd
import numpy as np

"""
This homework examplifies classification (of whikies) and datarepresentation with Bokeh 
"""
# First simply example
"""
This homework examplifies classification (of whikies) and datarepresentation with Bokeh 
"""
points = [(0,0), (1,2), (3,1)]
xs, ys = zip(*points)
colors = ["red", "blue", "green"]

bio.output_file("Spatial_Example.html", title="Regional Example")
location_source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
    }
)

fig = bplot.figure(title = "Title",
    x_axis_location = "above", tools="resize, hover, save")
fig.plot_width  = 300
fig.plot_height = 380
fig.circle("x", "y", 10, 10, size=10, source=location_source,
     color='colors', line_color = None)

hover = fig.select(dict(type = HoverTool))
hover.tooltips = {
    "Location": "(@x, @y)"
}
bplot.show(fig)

"""Whisky Example"""

#getting wiskey data
whisky = pd.read_csv("./whisky_data/whiskies.txt")
#add column Region
whisky["Region"] = pd.read_csv("./whisky_data/regions.txt")


plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# iterate over the  grid to plot with bokeh.
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)
# zip(*iterable) returns a list oc coordinate tuples eg zip(anArray[0:3, 0:3]) [(x0, y0),(x1, y1),(x2, y2)]
xs, ys = zip(*grid)

# colors-> list of colors, alternating between red and blue.
colors = [plot_colors[i%2] for i in range(len(grid))]

# alpha-> linear Transparancy gradient for the points of the grid where 0 is completely transparent.

alphas = np.linspace(0, 1, len(grid))

# Store Coordinates, alpha and color of each point in 'ColumnDataSource' object for Bokeh

source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)
# Voila ....plot it

bio.output_file("Basic_Example.html", title="Basic Example")
fig = bplot.figure(tools="resize, hover, save")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }
bio.show(fig)

#Define a set of colors corresponding to regions the whiskies come from for colored clustering
cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = {regions[r]:cluster_colors[r] for r in range(len(regions))}

#TODO: define correlations as a two-dimensional np.array with both rows and columns corresponding to distilleries and elements corresponding to the flavor correlation of each row/column pair (86x86)

distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i, j] < 0.7:                   # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if whisky.Group[i]==whisky.Group[j]:       # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.

#Plot correlation of flavor profilies among distilleries
source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "alphas": correlations.flatten(),
        "correlations": correlations.flatten(),
    }
)

bio.output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = bplot.figure(title="Whisky Correlations", x_axis_location="above", tools="resize,hover,save",
    x_range=list(reversed(distilleries)), y_range=distilleries)
fig.grid.grid_line_color = None


#Plot spacial distribution of distilleries
def location_plot(title, colors):
    bio.output_file(title+".html")
    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
            }
    )
    fig = bplot.figure(title = title, x_axis_location = "above", tools="resize, hover, save")
    fig.plot_width  = 400
    fig.plot_height = 500
    fig.circle("x", "y", 10, 10, size=9, source=location_source,
    color='colors', line_color = None)
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type = HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
        }
    bplot.show(fig)

region_cols = [region_colors[whisky.Region[i]] for i in range(len(whisky.Region))]
classification_cols = [cluster_colors[whisky.Group[i]] for i in range(len(whisky.Region))]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)
