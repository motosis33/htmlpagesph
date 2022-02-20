from flask import Flask, render_template
from matplotlib import artist
import numpy
import pandas as pd
import csv
from typing import List, Dict

top_artists = ["['Alla Pugacheva']", "['Aretha Franklin']", "['Bachata Klan']", "['Banda Black Rio']", "['Betty Davis']"]

workout = "Cardio"
intensity = "Moderate"
parameter = []

if (workout == "Flexibility"):
    parameter = [0.30, 0.50, 0.70, 0.90, -30.00, -20.00, 50.00, 75.00]
elif (workout == "Cardio"):
    if (intensity == "Moderate"):
        parameter = [0.60, 0.80, 0.50, 0.80, -25.00, -10.00, 100.00, 150.00]

    elif (intensity == "High"):
        parameter = [0.80, 1.00, 0.80, 1.00, -10.00, 0.50, 150.00, 200.00]

elif (workout == "Strength"):
    if (intensity == "Moderate"):
        parameter = [0.50, 0.80, 0.60, 0.80, -30.00, 20.00, 50.00, 100.00]
    elif (intensity == "High"):
        parameter = [0.80, 0.95, 0.80, 1.00, -20.00, -10.00, 100.00, 150.00]

filename = 'templates/Spotify Track Data Rounded.csv'
file = open(filename)
reader = csv.reader(file)
header = next(reader)

rows = []
for row in reader:
    rows.append(row)

artist_dataset = []

for row in rows:
    if (row[2] in top_artists):
        artist_dataset.append (row[1])
        artist_dataset.append(row[2])

main_array = numpy.array(artist_dataset) # converting to numpy array
out_array = main_array.take([0, 1, 4, 5, 6, 7])
out_list = out_array.tolist() # if you want a list specifically

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return str(out_list)

if __name__ == '__main__':
  app.run(debug=True)
