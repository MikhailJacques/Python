from docx import Document
import pandas as pd


def process_document(input_file, output_file):
    try:
        # Open the Word document
        doc = Document(input_file)
    except Exception as e:
        print(f"Error opening the Word document: {e}")
        return

    # Initialize a list to store the data
    data = []

    # Initialize variables to store the current heading and content
    current_heading_number = None
    current_heading_name = None
    current_content = ''

    # Loop through each paragraph in the document
    for para in doc.paragraphs:
        # Check if the paragraph is a heading
        if para.style.name.startswith('Heading'):
            # If we have a current heading, add it and its content to the data list
            if current_heading_number is not None and current_heading_name is not None:
                data.append([current_heading_number, current_heading_name, current_content.strip()])
            # Split the heading number from the heading name
            try:
                current_heading_number, current_heading_name = para.text.split(' ', 1)
            except ValueError as e:
                print(f"Error splitting heading number and name: {e}")
                continue
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
        df.to_excel(output_file, index=False)
    except Exception as e:
        print(f"Error writing to Excel file: {e}")


if __name__ == '__main__':
    process_document('Atp input.docx', 'Atp output.xlsx')
