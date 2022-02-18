from itertools import groupby
import pandas as pd
import plotly.graph_objects as go

file = pd.read_csv("data.csv")
studentData = file.loc[file['student_id']=='TRL_987']
analysis = studentData.groupby("level")['attempt'].mean()

figure = go.Figure(go.Bar(
    x= analysis,
    y= ['Level 1','Level 2', 'Level 3', 'Level 4'], 
    orientation= 'h'
))

figure.show()