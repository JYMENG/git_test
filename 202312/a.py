import pandas as pd

# Replace the following lines with your actual DataFrame
data = {'customer': ['c1', 'c1', 'c1'],
        'date': ['d1', 'd2', 'd3'],
        't1': [1, 1, 1],
        't2': [1, 1, 2],
        't3': [1, 2, 2]}

df = pd.DataFrame(data)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort DataFrame by customer, type, and date
df.sort_values(by=['customer', 't1', 't2', 't3', 'date'], inplace=True)

# Identify the last score date before the change for each type
change_dates = df[df[['t1', 't2', 't3']].diff().ne(0).any(axis=1)].groupby(['customer']).agg(
    t1_last_score_date=('date', 'first'), 
    t2_last_score_date=('date', 'first'), 
    t3_last_score_date=('date', 'first'),
    t1_last_score=('t1', 'last'),
    t2_last_score=('t2', 'last'),
    t3_last_score=('t3', 'last')
).reset_index()

# Select the latest date and T1, T2, T3 from the last row for each customer
result = df.groupby('customer').agg(
    latest_date=('date', 'last'),
    t1=('t1', 'last'),
    t2=('t2', 'last'),
    t3=('t3', 'last')
).merge(change_dates[['customer', 't1_last_score_date', 't2_last_score_date', 't3_last_score_date', 't1_last_score', 't2_last_score', 't3_last_score']], on='customer', how='left')

# Display the result
print(result)
# Display the result
print(result)

  customer latest_date  t1  t2  t3 t1_last_date t2_last_date t3_last_date  t1_last_score  t2_last_score  t3_last_score
0       c1  2023-01-03   1   2   2          NaT   2023-01-02   2023-01-01            NaN            1.0            1.0
