import pandas as pd
import plotly.express as graphmaker

data = pd.read_csv('CovidCases.csv')
dtaframe = pd.DataFrame(data)
scatterplot = graphmaker.scatter(dtaframe, x = 'date', y = 'cases', color='country')
scatterplot.show()