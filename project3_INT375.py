import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/abhaysingh/Downloads/WHO-COVID-19-global-data.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.fillna(0, inplace=True)

df['Month'] = df['Date_reported'].dt.to_period('M')

# Group by WHO region and month to get total new cases
heatmap_data = df.groupby(['WHO_region', 'Month'])['New_cases'].sum().unstack().fillna(0)

# Create heatmap
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="Reds", linewidths=0.5, linecolor='gray')
plt.title("Monthly COVID-19 Cases by WHO Region")
plt.xlabel("Month")
plt.ylabel("WHO Region")
plt.tight_layout()
plt.show()
