# Load Excel file
excel_file = 'your_excel_file.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='openpyxl')
excel_writer.book = load_workbook(excel_file)
excel_writer.sheets = dict((ws.title, ws) for ws in excel_writer.book.worksheets)

# Write DataFrame to Excel, append to existing table
df_json.to_excel(excel_writer, sheet_name='Sheet1', index=False, startrow=1, header=False)

# Save changes
excel_writer.save()