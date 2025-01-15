import os
from converter import pdf_to_text
from reportlab.pdfgen import canvas

def test_pdf_to_text():
    pdf_path = "sample.pdf"
    output_path = "output.txt"

    # Create a valid PDF file
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Hello, this is a test PDF.")
    c.save()

    # Call the function to convert the PDF to text
    pdf_to_text(pdf_path, output_path)

    # Assert that the output file was created and contains expected content
    assert os.path.exists(output_path)
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "Hello, this is a test PDF." in content

    # Clean up generated files
    os.remove(pdf_path)
    os.remove(output_path)