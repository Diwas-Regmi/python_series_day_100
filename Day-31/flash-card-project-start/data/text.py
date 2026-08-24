import pandas as pd
#
directory = "./data/french_words.csv"
df = pd.read_csv(directory)
print(df.iloc[index_rand]["French"])