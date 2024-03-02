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