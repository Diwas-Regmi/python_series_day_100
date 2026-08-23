import pandas as pd
df = pd.read_csv("Central_Park_Squirrel_Census.csv")
# print(df.head())
fur_counts = df["Primary Fur Color"].value_counts()
print(fur_counts)
fur_counts.to_csv("Squirrel_count.csv")
# fur_row = df[df["Primary Fur Color"] == "Black"]
# print(fur_row)
print(len(df["Primary Fur Color"] == "Gray"))
print(len(df[df["Primary Fur Color"] == "Gray"]))