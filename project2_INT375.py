import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/abhaysingh/Downloads/WHO-COVID-19-global-data.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.fillna(0, inplace=True)

# Objective 3: Compare Regional Responses
region_trends = df.groupby(['Date_reported', 'WHO_region'])[['New_cases']].sum().reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(data=region_trends, x='Date_reported', y='New_cases', hue='WHO_region')
plt.title('COVID-19 New Cases by WHO Region Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend(title='WHO Region')
plt.show()
