import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('your_xml_file.xml')
root = tree.getroot()

# Open a CSV file in write mode
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write headers based on the XML tags
    headers = []
    for child in root[0]:
        headers.append(child.tag)
    csvwriter.writerow(headers)

    # Write data to CSV
    for item in root.findall('.//item'):
        row = []
        for child in item:
            row.append(child.text)
        csvwriter.writerow(row)

print("CSV file created successfully!")