from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
import logging
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'models')))

from models.pdf_converter import pdf_to_markdown, save_markdown_to_file, markdown_to_pdf
from models.llm import generate_optimized_resume

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/upload/")
async def upload_and_download_resume(
    file: UploadFile = File(...), 
    job_description: str = Form(...)
):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File '{file.filename}' uploaded successfully with job description.")

        md_content = pdf_to_markdown(file_location)
        print("Extracted Markdown Content:\n", md_content)

        optimized_markdown = generate_optimized_resume(md_content, job_description)
        print("Optimized Markdown Content:\n", optimized_markdown)

        markdown_file = save_markdown_to_file(optimized_markdown, "Optimized_Resume.md")

        pdf_file = os.path.join(OUTPUT_DIR, "Formatted_Resume.pdf")
        markdown_to_pdf(markdown_file, pdf_file)

        return FileResponse(
            path=pdf_file,
            filename="Optimized_Resume.pdf",
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=Optimized_Resume.pdf"}
        )
    
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
