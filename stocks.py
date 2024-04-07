import matplotlib.pyplot as plt
import pandas as pd
import json
from datetime import datetime, timedelta

# Load the JSON data from the file
file_path = './stocks.json'  # Replace with your file path
with open(file_path, 'r') as file:
    stocks_data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(stocks_data['historical'])

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Calculate 30 and 60 days ago from the latest date in the data
latest_date = df['date'].max()
date_30_days_ago = latest_date - timedelta(days=30)
date_60_days_ago = latest_date - timedelta(days=60)

# Filter the DataFrame for the last 30 days and calculate average high and low
df_last_30_days = df[df['date'] > date_30_days_ago]
average_high = df_last_30_days['high'].mean()
average_low = df_last_30_days['low'].mean()

# Filter the DataFrame for the last 60 days and find the lowest value
df_last_60_days = df[df['date'] > date_60_days_ago]
lowest_value_60_days = df_last_60_days['low'].min()

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot for last 60 days
df_last_60_days.plot(x='date', y='low', ax=ax, label='Low (Last 60 Days)', color='blue')

# Highlight the lowest value in the last 60 days
lowest_date_60_days = df_last_60_days[df_last_60_days['low'] == lowest_value_60_days]['date']
ax.scatter(lowest_date_60_days, [lowest_value_60_days] * len(lowest_date_60_days), color='red', label='Lowest Value (60 Days)')

# Plot for last 30 days
df_last_30_days.plot(x='date', y='high', ax=ax, label='High (Last 30 Days)', color='green')
df_last_30_days.plot(x='date', y='low', ax=ax, label='Low (Last 30 Days)', color='orange')

# Labeling
ax.set_title('Stock Prices over the Last 60 Days')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()

# Show plot
plt.show()
