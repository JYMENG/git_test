import pandas as pd

# Assuming df is your DataFrame with columns ID, Date, Type A, Type B, Type C, and Value
# Replace 'ID', 'Date', 'Type A', 'Type B', 'Type C', 'Value' with your actual column names

# Convert the 'Date' column to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Find the latest date and corresponding value for each type for each customer
latest_values = df.groupby('ID').apply(lambda group: group.loc[group['Date'].idxmax()])

# Find the last date when the value changes for each type for each customer
last_date_changed = pd.DataFrame()

for col in ['Type A', 'Type B', 'Type C']:
    mask = latest_values[col] != latest_values.groupby('ID')[col].shift()
    changed_values = latest_values.loc[mask, ['ID', 'Date', col]]
    last_date_changed = pd.concat([last_date_changed, changed_values])

# Display the results
print("Latest Date and Corresponding Value for Each Type for Each Customer:")
print(latest_values)

print("\nLast Date When the Value Changes for Each Type for Each Customer:")
print(last_date_changed)
