from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import shutil
import logging
from models.pdf_converter import pdf_to_markdown, save_latex_to_file, compile_latex_to_pdf
from models.llm import generate_optimized_resume

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/upload/")
async def upload_file_with_job_desc(
    file: UploadFile = File(...), 
    job_description: str = Form(...)
):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File '{file.filename}' uploaded successfully with job description.")
        
        # Convert PDF to Markdown
        md_content = pdf_to_markdown(file_location)
        
        # Generate optimized resume in LaTeX format
        latex_resume = generate_optimized_resume(md_content, job_description)
        
        # Save LaTeX to file and compile to PDF
        save_latex_to_file(latex_resume)
        compile_latex_to_pdf("resume.tex")
        
        return {
            "filename": file.filename,
            "job_description": job_description,
            "status": "processed",
            "latex_resume": latex_resume
        }
    
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="File upload failed")

