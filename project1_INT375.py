import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/abhaysingh/Downloads/WHO-COVID-19-global-data.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.fillna(0, inplace=True)

# Objective 2: Identify Hotspots
latest_date = df['Date_reported'].max()
latest_data = df[df['Date_reported'] == latest_date]
hotspots = latest_data.sort_values(by='Cumulative_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='Cumulative_cases', y='Country', data=hotspots, hue='Country', palette='Reds_r', legend=False)
plt.title('Top 10 Countries with Highest Cumulative COVID-19 Cases')
plt.xlabel('Cumulative Cases')
plt.ylabel('Country')
plt.show()
