import pandas as pd

# Assuming your DataFrame is named 'df'
# Replace 'customer', 'date', 'typeA', 'typeB', 'typeC' with your actual column names

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort DataFrame by customer, type, and date
df.sort_values(by=['customer', 'typeA', 'typeB', 'typeC', 'date'], inplace=True)

# Find the last date when the score changes for each type and customer
last_change_dates = df[df[['typeA', 'typeB', 'typeC']].diff().ne(0).any(axis=1)].groupby(['customer']).agg(
    typeA_last_change=('date', 'last'), 
    typeB_last_change=('date', 'last'), 
    typeC_last_change=('date', 'last')
).reset_index()

# Display the result
print(last_change_dates)
