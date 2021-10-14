import os
os.system('pip install numpy')
os.system('pip install matplotlib')
os.system('pip install numpy')
os.system('pip install requests')
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import requests

url = "https://github.com/Jminding/ChemistryChromatographyLab/releases/download/v0.1/Chromatography.Lab0.1.-.Sheet1.csv"
r = requests.get(url, allow_redirects=True)
file = open("ChromatographyLab0.1-Sheet1.csv", "wb")
file.write(r.content)
file.close()
file = open('ChromatographyLab0.1-Sheet1.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
file.close()
for i in range(len(rows)):
    for j in range(len(rows[i])):
        try:
            rows[i][j] = float(rows[i][j])
        except Exception:
            rows[i][j] = 0 # 0 represents that it wasn't used in the trial
for i in range(len(rows)):
    del rows[i][0]
print(rows)
red = []
orange = []
yellow = []
green = []
blue = []
for i in range(len(rows)):
    red.append(rows[i][0])
    orange.append(rows[i][1])
    yellow.append(rows[i][2])
    green.append(rows[i][3])
    blue.append(rows[i][4])
print(rows)
plt.xticks([1, 2, 3])
plt.plot([1, 2, 3], red, color="red")
plt.plot([1, 2, 3], orange, color="orange")
plt.plot([1, 2, 3], yellow, color="#fff700")
plt.plot([1, 2, 3], green, color="green")
plt.plot([1, 2, 3], blue, color="blue")
custom_lines = [Line2D([0], [0], color="red", lw=4),
                Line2D([0], [0], color="orange", lw=4),
                Line2D([0], [0], color="#fff700", lw=4),
                Line2D([0], [0], color="green", lw=4),
                Line2D([0], [0], color="blue", lw=4),]
plt.legend(custom_lines, ["Red", "Orange", "Yellow", "Green", "Blue"], prop={"size": 9})
plt.show()
