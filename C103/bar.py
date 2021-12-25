import pandas as ps
import plotly.express as pl
df = ps.read_csv("data.csv")
figure = pl.bar(df,x = "Country", y = "InternetUsers")
figure.show()