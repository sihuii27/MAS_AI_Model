from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    extract_text = ""
    for pdf in pdf_file:
        reader = PdfReader(pdf)
        for page in reader.pages:
            extract_text += page.extract_text() + "\n"
    return extract_text