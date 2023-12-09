import pandas as pd

# Assuming your DataFrame is named 'df'
# Replace 'customer', 'date', 'typeA', 'typeB', 'typeC' with your actual column names

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort DataFrame by customer, type, and date
df.sort_values(by=['customer', 'typeA', 'typeB', 'typeC', 'date'], inplace=True)

# Find the last date when the score changes for each type and customer
change_dates = df[df[['typeA', 'typeB', 'typeC']].diff().ne(0).any(axis=1)].groupby(['customer']).agg(
    typeA_last_change=('date', 'last'), 
    typeB_last_change=('date', 'last'), 
    typeC_last_change=('date', 'last')
).reset_index()

# Merge with unique customer and type combinations to ensure all combinations are included
result = pd.merge(pd.MultiIndex.from_product([df['customer'].unique(), df['typeA'].unique(), df['typeB'].unique(), df['typeC'].unique()], names=['customer', 'typeA', 'typeB', 'typeC']), 
                  change_dates, how='left', on='customer')

# Display the result
print(result)
