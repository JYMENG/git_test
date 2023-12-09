import pandas as pd

# Replace the following lines with your actual DataFrame
data = {'customer_id': ['c1', 'c1', 'c1'],
        'idp_effective_date': ['d1', 'd2', 'd3'],
        'TYPE1': [1, 1, 1],
        'TYPE2': [1, 1, 2],
        'TYPE3': [1, 2, 2]}

df = pd.DataFrame(data)

# Convert 'idp_effective_date' column to datetime format
df['idp_effective_date'] = pd.to_datetime(df['idp_effective_date'])

# Sort DataFrame by customer, type, and date
df.sort_values(by=['customer_id'] + df.columns[2:].tolist() + ['idp_effective_date'], inplace=True)

# Identify the last score date before the change for each type
change_dates = df[df.iloc[:, 2:].diff().ne(0).any(axis=1)].groupby(['customer_id']).agg(
    **{f'{col}_last_score_date': ('idp_effective_date', 'first') for col in df.columns[2:]},
    **{f'{col}_last_score': (col, 'first') for col in df.columns[2:]}
).reset_index()

# Select the latest date and types from the last row for each customer
result = df.groupby('customer_id').agg(
    latest_date=('idp_effective_date', 'last'),
    **{f'{col}': (col, 'last') for col in df.columns[2:]}
).merge(change_dates, on='customer_id', how='left')

# Update last score date and last score to blank if they are the same as the latest score
for col in df.columns[2:]:
    if result[f'{col}_last_score'] == result[col]:
        result[f'{col}_last_score_date'] = ''
        result[f'{col}_last_score'] = ''

# Display the result
print(result)
