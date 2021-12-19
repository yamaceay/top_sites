import pandas as pd

df = pd.read_csv("site_data.csv").set_index("Rank")

# df["% of Traffic From Search"] = df["% of Traffic From Search"].map(lambda x: float(x[:-1])/100)

# df["Daily Pageviews per Visitor"] = df["Daily Pageviews per Visitor"].astype(float)

# df.to_csv("site_data.csv")

print(df)
