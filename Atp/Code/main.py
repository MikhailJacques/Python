from docx import Document
import pandas as pd
import re

try:
    # Open the Word document
    doc = Document('Atp input.docx')
except Exception as e:
    print(f"Error opening the Word document: {e}")
    exit(1)

# Initialize a list to store the data
data = []

# Initialize variables to store the current heading and content
current_heading_number = None
current_heading_name = None
current_content = ''

# Loop through each paragraph in the document
for para in doc.paragraphs:
    # # Check if the paragraph is a heading
    # if para.style.name.startswith('Heading'):
    #     # If we have a current heading, add it and its content to the data list
    #     if current_heading_number is not None and current_heading_name is not None:
    #         data.append([current_heading_number, current_heading_name, current_content.strip()])
    #     # Split the heading number from the heading name
    #     try:
    #         current_heading_number, current_heading_name = para.text.split(' ', 1)
    #     except ValueError as e:
    #         print(f"Error splitting heading number and name: {e}")
    #         continue
    #     # Reset the content string
    #     current_content = ''

    # # Check if the paragraph is a heading
    # if para.style.name.startswith('Heading'):
    #     # If we have a current heading, add it and its content to the data list
    #     if current_heading_number is not None and current_heading_name is not None:
    #         data.append([current_heading_number, current_heading_name, current_content.strip()])
    #     # Split the heading number from the heading name
    #     split_heading = para.text.split(' ', 1)
    #     if len(split_heading) == 2:
    #         current_heading_number, current_heading_name = split_heading
    #     else:
    #         print(f"Warning: Heading does not contain a space: {para.text}")
    #         current_heading_number = None
    #         current_heading_name = para.text
    #     # Reset the content string
    #     current_content = ''

    # # Check if the paragraph is a heading
    # if para.style.name.startswith('Heading'):
    #     # If we have a current heading, add it and its content to the data list
    #     if current_heading_number is not None and current_heading_name is not None:
    #         data.append([current_heading_number, current_heading_name, current_content.strip()])
    #     # Split the heading number from the heading name
    #     split_heading = re.split('\s', para.text, 1)
    #     if len(split_heading) == 2:
    #         current_heading_number, current_heading_name = split_heading
    #     else:
    #         print(f"Warning: Heading does not contain a space: {para.text}")
    #         current_heading_number = None
    #         current_heading_name = para.text
    #     # Reset the content string
    #     current_content = ''

    # Check if the paragraph is a heading
    if para.style.name.startswith('Heading'):
        # If we have a current heading, add it and its content to the data list
        if current_heading_number is not None and current_heading_name is not None:
            data.append([current_heading_number, current_heading_name, current_content.strip()])
        # Split the heading number from the heading name
        split_heading = re.split(r'\s', para.text, 1)
        if len(split_heading) == 2:
            current_heading_number, current_heading_name = split_heading
        else:
            print(f"Warning: Heading does not contain a space: {para.text}")
            current_heading_number = None
            current_heading_name = para.text
        # Reset the content string
        current_content = ''
    else:
        # Add the paragraph text to the content string
        current_content += para.text + '\n'

# Add the last heading and its content to the data list
if current_heading_number is not None and current_heading_name is not None:
    data.append([current_heading_number, current_heading_name, current_content.strip()])

# Convert the data list to a DataFrame
df = pd.DataFrame(data, columns=['Heading Number', 'Heading Name', 'Content'])

# Write the DataFrame to an Excel file
try:
    df.to_excel('Atp output.xlsx', index=False)
except Exception as e:
    print(f"Error writing to Excel file: {e}")
    exit(1)
