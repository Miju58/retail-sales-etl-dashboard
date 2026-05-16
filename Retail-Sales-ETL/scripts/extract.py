import pandas as pd

sales = pd.read_csv("./data/Superstore.csv", encoding="latin1")

print(sales.head())