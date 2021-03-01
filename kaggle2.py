import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("deliveries.csv")
fig = ff.create_distplot([df["over"].tolist()], ["Overs Bowled by the Bowler"], show_hist = False)
fig.show()