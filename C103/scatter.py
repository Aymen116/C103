import pandas as ps
import plotly.express as pl
df = ps.read_csv("data.csv")
figure = pl.scatter(df,x = "Population" , y="InternetUsers")
figure.show()