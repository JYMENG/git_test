# Load Excel file
excel_file = 'your_excel_file.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='openpyxl')
excel_writer.book = load_workbook(excel_file)
excel_writer.sheets = dict((ws.title, ws) for ws in excel_writer.book.worksheets)

# Write DataFrame to Excel, append to existing table
df_json.to_excel(excel_writer, sheet_name='Sheet1', index=False, startrow=1, header=False)

# Save changes
excel_writer.save()




import pandas as pd

# Read JSON file into pandas DataFrame
df_json = pd.read_json('your_json_file.json')

# Load Excel file and select the sheet
excel_file = 'your_excel_file.xlsx'
sheet_name = 'Sheet1'  # Replace 'Sheet1' with the actual sheet name
excel_data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Update the existing table in Excel with the new data
with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl') as writer:
    writer.book = openpyxl.load_workbook(excel_file)
    writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
    df_json.to_excel(writer, sheet_name=sheet_name, startrow=len(excel_data)+1, index=False, header=False)
    
    
    
    
    
    
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

# Load the existing Excel file
excel_file = "your_excel_file.xlsx"
wb = load_workbook(excel_file)
ws = wb.active

# Sample DataFrame with new data
new_data = {
    'Name': ['Tom', 'Emma'],
    'Age': [40, 28],
    'City': ['Seattle', 'San Francisco']
}
df_new = pd.DataFrame(new_data)

# Determine the range of the existing table (assuming it starts from A1)
table_range = f"A1:{chr(ord('A') + len(df_new.columns) - 1)}1"

# Write new data from DataFrame to worksheet
for r in dataframe_to_rows(df_new, index=False, header=False):
    ws.append(r)

# Update the table range to include the new data
new_table_range = f"{table_range.split(':')[0]}:{chr(ord('A') + len(df_new.columns) - 1)}{len(df_new) + 1}"

# Save the workbook
wb.save(excel_file)