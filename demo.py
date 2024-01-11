from datetime import date
import pandas as pd

print(date.today())
df=pd.read_csv("holiday.csv")
day=date.today()
for i in df["day"]:
    if i==str(day):
        print("its wokring")

