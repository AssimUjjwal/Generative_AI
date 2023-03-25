import PyPDF2

# Open the PDF file in binary mode
with open('Assim_Ujjwal_SDE_Resume.pdf', 'rb') as file:

    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF file
    num_pages = len(reader.pages)

    # Loop through each page and extract the text
    for i in range(num_pages):
        page = reader.pages[i]
        text = page.extract_text()

        with open('output.txt', 'w') as f:
            with f:
                f.write(text)
                
