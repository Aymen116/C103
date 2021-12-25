import pandas as ps
import plotly.express as pl
# data = [1,2,3,4]
# df = ps.DataFrame(data)
# print(df)
df = ps.read_csv("data.csv")
figure = pl.line(df,x = "Country", y = "InternetUsers")
figure.show()