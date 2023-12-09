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
df.sort_values(by=['customer', 'TYPE1', 'TYPE2', 'TYPE3', 'date'], inplace=True)

# Identify the last score date before the change for each type
change_dates = df[df[['TYPE1', 'TYPE2', 'TYPE3']].diff().ne(0).any(axis=1)].groupby(['customer']).agg(
    TYPE1_last_score_date=('date', 'first'),
    TYPE2_last_score_date=('date', 'first'),
    TYPE3_last_score_date=('date', 'first'),
    TYPE1_last_score=('TYPE1', 'last'),
    TYPE2_last_score=('TYPE2', 'last'),
    TYPE3_last_score=('TYPE3', 'last')
).reset_index()

# Select the latest date and types from the last row for each customer
result = df.groupby('customer').agg(
    latest_date=('date', 'last'),
    TYPE1=('TYPE1', 'last'),
    TYPE2=('TYPE2', 'last'),
    TYPE3=('TYPE3', 'last')
).merge(change_dates, on='customer', how='left')

# Update last score date and last score to blank if they are the same as the latest score
for col in ['TYPE1', 'TYPE2', 'TYPE3']:
    if result[f'{col}_last_score'] == result[col]:
        result[f'{col}_last_score_date'] = ''
        result[f'{col}_last_score'] = ''

# Display the result
print(result)
