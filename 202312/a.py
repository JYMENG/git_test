import pandas as pd

# Replace the following lines with your actual DataFrame
data = {'customer': ['c1', 'c1', 'c1'],
        'date': ['d1', 'd2', 'd3'],
        'TYPE1': [1, 1, 1],
        'TYPE2': [1, 1, 2],
        'TYPE3': [1, 2, 2]}

df = pd.DataFrame(data)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort DataFrame by customer, type, and date
df.sort_values(by=['customer'] + [col for col in df.columns if 'TYPE' in col] + ['date'], inplace=True)

# Identify the last score date before the change for each type
change_dates = df[df.filter(regex='^TYPE\d').diff().ne(0).any(axis=1)].groupby(['customer']).agg(
    **{f'{col}_last_score_date': ('date', 'first') for col in df.filter(regex='^TYPE\d').columns},
    **{f'{col}_last_score': (col, 'last') for col in df.filter(regex='^TYPE\d').columns}
).reset_index()

# Select the latest date and types from the last row for each customer
result = df.groupby('customer').agg(
    latest_date=('date', 'last'),
    **{f'{col}': (col, 'last') for col in df.filter(regex='^TYPE\d').columns}
).merge(change_dates, on='customer', how='left')

# Update⬤
