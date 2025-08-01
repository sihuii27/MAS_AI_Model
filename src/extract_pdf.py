from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    extract_text = ""
    for pdf in pdf_file:
        print(f"Processing file: {pdf.name}")
        reader = PdfReader(pdf)
        extract_text += f"\n\n===== File: {pdf.name} =====\n\n"
        for page in reader.pages:
            extract_text += page.extract_text() + "\n"
        extract_text += f"\n\n===== End of file: {pdf.name} =====\n\n"
    return extract_text