# Resume Optimizer AI

Resume Optimizer AI is an intelligent web application that optimizes resumes based on specific job descriptions. Users can upload their resumes in PDF format, provide job descriptions, and receive tailored resumes optimized for job applications. The application leverages **FastAPI** for the backend, **WeasyPrint** for PDF generation, and **Groq AI** for intelligent resume optimization.

## 🚀 Features

- 📂 **Upload Resume**: Upload resumes in **PDF format**.
- 📝 **Provide Job Description**: Enter job descriptions to tailor your resume accordingly.
- 📜 **Resume Optimization**: AI refines and enhances resumes based on the job role.
- 🔄 **Generate Optimized Resume**: Get the final optimized resume in **Markdown** and **PDF formats**.
- 🌐 **User-Friendly Interface**: Simple web interface for seamless user interaction.

## 🏗️ Project Structure

```
Resume-Optimizer/
├── backend/
│   ├── models/
│   │   ├── llm.py             # AI model for resume optimization
│   │   ├── pdf_converter.py   # Converts optimized resume to PDF
│   │ 
│   ├── outputs/
│   │   └── Optimized_Resume.md # Stores optimized resume in Markdown format
│   ├── uploads/               # Stores uploaded resumes
│   ├── app.py                 # FastAPI application entry point
│   ├── requirements.txt       # Backend dependencies
│   └── test.py                # Unit tests for backend
├── frontend/
│   └── index.html             # Web interface
└── .gitignore                 # Ignore unnecessary files
```

## ⚡ Installation Guide

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/naveennk045/Resume-Optimizer
cd Resume-Optimizer
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r backend/requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the `backend` directory and add your **Groq API key**:
```
GROQ_API_KEY=your_groq_api_key
```

## 🛠️ Usage Instructions

### 1️⃣ Start the FastAPI Server
```sh
cd backend
uvicorn app:app --reload
```

### 2️⃣ Access the Web Interface
Open `frontend/index.html` in your browser and interact with the application.

### 3️⃣ Optimize Your Resume
- Upload your resume (PDF format).
- Provide the job description.
- Download the AI-optimized resume in **Markdown** or **PDF** format.

## 📡 API Endpoints

### 🔹 **Upload Resume & Optimize**
**Endpoint:** `POST /upload/`

**Parameters:**
- `file`: Resume in **PDF format**.
- `job_description`: Text describing the job role.

**Response:** Optimized resume in **PDF format**.

## 🎥 Demo

Watch the demo video to see the Resume Optimizer AI in action: [Demo Video](resume-optimizer-demo.mp4)

## 🎯 Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements:
- Open an issue
- Submit a pull request

Make sure to follow best practices and test your changes before submitting.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🤝 Acknowledgments

- **FastAPI**: For building the high-performance backend.
- **WeasyPrint**: For seamless PDF generation.
- **Groq AI**: For intelligent resume optimization.

🚀 Happy Coding! 🚀
