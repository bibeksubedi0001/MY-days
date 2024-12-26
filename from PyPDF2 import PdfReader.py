from PyPDF2 import PdfReader
from googletrans import Translator
from docx import Document

# Path to the PDF and the resulting Word document
pdf_path = r"C:\Users\Bibek\Downloads\unit-4-Main.pdf"
docx_path = r"C:\Users\Bibek\Downloads\unit-4-Main-Nepali.docx"

# Initialize the translator
translator = Translator()

# Create a new Document
doc = Document()

# Read the PDF file
reader = PdfReader(pdf_path)

# Iterate through each page, extract the text, translate it in small chunks
for page in reader.pages:
    text = page.extract_text()
    
    # Split the text into smaller parts (by sentences or paragraphs)
    paragraphs = text.split("\n")
    
    for para in paragraphs:
        # Translate each paragraph separately
        translated_text = translator.translate(para, src='en', dest='ne').text
        doc.add_paragraph(translated_text)

# Save the document as a .docx file
doc.save(docx_path)

print(f"Translated Word document saved at: {docx_path}")
