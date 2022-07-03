import pandas as pd

df = pd.read_csv("~/Desktop/pantheon.tsv", delimiter="\t")
df1 = df[["name", "countryCode3", "gender", "HPI"]]
df1 = df1.head(201)
df1.to_csv("~/Desktop/redis_dataset.csv", index=False)

print(df1)
