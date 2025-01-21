from flask import Flask, request, send_file, render_template
import os
import pdfplumber

app = Flask(__name__)
UPLOAD_FOLDER = '/app/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'pdf' not in request.files:
        return "No file uploaded", 400
    
    pdf_file = request.files['pdf']
    if not pdf_file.filename.endswith('.pdf'):
        return "Invalid file type", 400

    # Save uploaded file
    input_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(input_path)

    # Convert PDF to text
    output_path = input_path.replace('.pdf', '.txt')
    with pdfplumber.open(input_path) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    # Send converted file back to user
    return send_file(output_path, as_attachment=True)

# The block below is optional for local development but will be ignored by Gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
