from flask import Flask, request, jsonify, send_file
import os
from models.pdf_converter import pdf_to_markdown, markdown_to_pdf
from models.deepseek import response  

app = Flask(__name__)

UPLOAD_FOLDER = r"V:\Projects\Resume-Optimizer\backend\uploads"
OUTPUT_FOLDER = r"V:\Projects\Resume-Optimizer\backend\outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/optimize-resume', methods=['POST'])
def optimize_resume():
    if 'resume' not in request.files or 'jobDescription' not in request.form:
        return jsonify({"error": "Missing resume file or job description"}), 400
    
    file = request.files['resume']
    job_description = request.form['jobDescription']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    markdown_resume = pdf_to_markdown(file_path)

    optimized_markdown = response(markdown_resume, job_description)

    output_pdf_path = os.path.join(OUTPUT_FOLDER, "optimized_resume.pdf")
    markdown_to_pdf(optimized_markdown, output_pdf_path)

    os.remove(file_path)

    return send_file(output_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
