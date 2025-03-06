import markdown
from weasyprint import HTML
import os

def markdown_to_pdf(input_md, output_pdf, css_path=None):
    """
    Convert a Markdown file or string to a well-formatted PDF.
    
    Args:
        input_md (str): Path to the Markdown file or Markdown string.
        output_pdf (str): Path where the output PDF will be saved.
        css_path (str, optional): Path to a custom CSS file for styling.
    """
    # Step 1: Read the Markdown content (if it's a file)
    if os.path.isfile(input_md):
        with open(input_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
    else:
        md_content = input_md

    # Step 2: Convert Markdown to HTML
    # Enable extensions for better formatting (tables, code highlighting, etc.)
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
    html_content = md.convert(md_content)

    # Step 3: Define default CSS for good formatting
    default_css = """
    @page {
        size: A4;
        margin: 2cm;
    }
    body {
        font-family: Arial, sans-serif;
        font-size: 12pt;
        line-height: 1.6;
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }
    h1 {
        font-size: 24pt;
        border-bottom: 2px solid #2c3e50;
    }
    h2 {
        font-size: 20pt;
        border-bottom: 1px solid #ddd;
    }
    p {
        margin: 0.5em 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1em 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f4f4f4;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 4px;
        font-family: "Courier New", monospace;
    }
    pre {
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 4px;
        overflow-x: auto;
    }
    .codehilite {
        background-color: #f4f4f4;
    }
    """

    # Step 4: Use custom CSS if provided, otherwise use default
    if css_path and os.path.isfile(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
    else:
        css = default_css

    # Step 5: Combine HTML and CSS
    html_with_style = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>{css}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Step 6: Convert HTML to PDF
    HTML(string=html_with_style).write_pdf(output_pdf)

    print(f"PDF generated successfully at: {output_pdf}")

# Example usage
if __name__ == "__main__":
    # Example Markdown content (you can also pass a file path)
    sample_md = """
    # Sample Document

    This is a **sample** Markdown document to test the conversion to PDF.

    ## Section 1
    Here is some text in a paragraph. Below is a table:

    | Name  | Age | City     |
    |-------|-----|----------|
    | Alice | 25  | New York |
    | Bob   | 30  | London   |

    ### Code Example
    ```python
    def hello_world():
        print("Hello, World!")"""
    markdown_to_pdf(sample_md, 'output.pdf')
    