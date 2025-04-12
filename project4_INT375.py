import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/abhaysingh/Downloads/WHO-COVID-19-global-data.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.fillna(0, inplace=True)

# Maximum cumulative cases and deaths per region
summary = df.groupby('WHO_region')[['Cumulative_cases', 'Cumulative_deaths']].max()

# Calculate death rate percentage
summary['Death_Rate (%)'] = (summary['Cumulative_deaths'] / summary['Cumulative_cases']) * 100

# Display summary table
print("Summary Statistics by WHO Region:\n")
print(summary)
