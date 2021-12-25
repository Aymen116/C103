import pandas as ps
import plotly.express as pl
df = ps.read_csv("line_chart.csv")
figure = pl.bar(df, x="Country" , y="Per capita income")
figure.show()