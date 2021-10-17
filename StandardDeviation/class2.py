import csv
import pandas as pd
import plotly_express as px
with open('class2.csv' , newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
total_marks = 0
total_entry = (len(file_data))
for marks in file_data:
    total_marks+=float(marks[1])
mean = total_marks/total_entry
print("Mean is "+ str(mean))
df = pd.read_csv("class2.csv")
fig = px.line(df , x="Student Number" , y = "Marks")
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = mean,y1 = mean,
        x0 = 0 , x1 = total_entry
        
    )
])
fig.update_yaxes(rangemode = "tozero")
fig.show()