import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2015,2016,2017,2018,2019,2020,2021,2022,2023],
    "Net Income (USD Millions)": [12193,16798,21204,16571,39240,44281,61271,72738,72361]
}

df = pd.DataFrame(data)

df["YoY Growth %"] = df["Net Income (USD Millions)"].pct_change() * 100

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.bar(df["Year"], df["Net Income (USD Millions)"])
ax1.set_title("Microsoft Annual Net Income")
ax1.set_ylabel("USD Millions")

colors = df["YoY Growth %"].apply(lambda x: "green" if x > 0 else "red")
ax2.bar(df["Year"], df["YoY Growth %"], color=colors)
ax2.set_title("YoY Growth %")
ax2.set_ylabel("%")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output.png")
plt.show()
