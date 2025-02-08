import fitz  # PyMuPDF
import markdown
from fpdf import FPDF
import os
import re


def pdf_to_markdown(pdf_path):
    """Extract text from a PDF and convert it to Markdown format."""
    md_content = ""

    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text:
            md_content += f"## Page {page_num}\n\n{text}\n\n"

    return md_content


def clean_text(text):
    """Replace special characters and remove unsupported Unicode characters."""
    text = text.replace("–", "-") 
    text = text.replace("’", "'") 
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
    return text


def markdown_to_pdf(markdown_text, output_path):
    """Convert Markdown text to a PDF file while ensuring Unicode support."""
    pdf = FPDF()
    pdf.add_page()

    font_path = r"V:\Projects\Resume-Optimizer\fonts\DejaVuSans.ttf"  
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file '{font_path}' not found. Download it from https://dejavu-fonts.github.io/")

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    clean_md = clean_text(markdown_text)  
    pdf.multi_cell(0, 5, clean_md)  
    pdf.output(output_path)
    print(f"PDF saved successfully at: {output_path}")


if __name__ == "__main__":
    pdf_path = r"V:\Projects\Resume-Optimizer\backend\uploads\Naveenkumar_Resume(Updated).pdf"
    output_pdf_path = r"V:\Projects\Resume-Optimizer\backend\outputs\Converted_Resume.pdf"

    md_content = pdf_to_markdown(pdf_path)
    print(md_content)

    markdown_to_pdf(md_content, output_pdf_path)
