import pdfplumber
from docx import Document

def pdf_to_text(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages])
    with open(output_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    print(f"Text saved to {output_path}")

def pdf_to_word(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        doc = Document()
        for page in pdf.pages:
            doc.add_paragraph(page.extract_text())
        doc.save(output_path)
    print(f"Word document saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert PDF to Text or Word")
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("output", help="Path to the output file (with .txt or .docx extension)")
    args = parser.parse_args()

    if args.output.endswith(".txt"):
        pdf_to_text(args.input, args.output)
    elif args.output.endswith(".docx"):
        pdf_to_word(args.input, args.output)
    else:
        print("Output file must end with .txt or .docx")