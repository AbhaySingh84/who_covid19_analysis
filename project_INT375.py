import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/abhaysingh/Downloads/WHO-COVID-19-global-data.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.fillna(0, inplace=True)

# Objective 1: Analyze Global Trends
global_daily = df.groupby('Date_reported')[['New_cases', 'New_deaths']].sum()
global_cumulative = df.groupby('Date_reported')[['Cumulative_cases', 'Cumulative_deaths']].sum()

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(global_daily.index, global_daily['New_cases'], label='Daily New Cases')
plt.plot(global_daily.index, global_daily['New_deaths'], label='Daily New Deaths')
plt.legend()
plt.title('Global Daily COVID-19 Cases and Deaths')

plt.subplot(1, 2, 2)
plt.plot(global_cumulative.index, global_cumulative['Cumulative_cases'], label='Cumulative Cases')
plt.plot(global_cumulative.index, global_cumulative['Cumulative_deaths'], label='Cumulative Deaths')
plt.legend()
plt.title('Global Cumulative COVID-19 Cases and Deaths')
plt.tight_layout()
plt.show()
