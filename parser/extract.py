import pdfplumber

def extract_text_from_pdf(pdf_file):
    full_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text