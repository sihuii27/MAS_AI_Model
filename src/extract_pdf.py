import pdfplumber

def extract_text_from_pdf(pdf_file):
    extract_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extract_text += page.extract_text() + "\n"
    return extract_text