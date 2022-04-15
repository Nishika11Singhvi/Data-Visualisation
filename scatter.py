import pandas as pd
import plotly.express as px

df=pd.read_csv("scatter 103.csv")
fig=px.scatter(df, x="date", y="cases", color="country", size="cases", title="COVID 19 Data for Countries")
fig.show()