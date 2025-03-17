import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

PROMPT_TEMPLATE = """
You are a professional resume optimizer specializing in creating ATS-friendly Markdown resumes. I have a resume in Markdown and a job description. Optimize the resume to align precisely with the job requirements and return a well-structured Markdown document with clearly defined sections.

### Optimization Guidelines:
1. **Structure**: Output the resume in Markdown with the following sections in this order (if applicable based on input):
     Name should be top of the resume with larger font in center.
     After name give  email, phone, LinkedIn (if available).
   - **Professional Summary**: A concise 2-3 sentence summary tailored to the job description.
   - **Skills**: A bulleted list of relevant skills (technical and soft) matching the job description.
   - **Professional Experience**: Jobs in reverse chronological order with role, company, dates, and bullet points for achievements (quantify where possible, e.g., "Increased efficiency by 30%").
   - **Education**: Degree, institution, and graduation year.
   - **Projects** (optional): Relevant projects with brief descriptions and outcomes.
   - **Certifications** (optional): Relevant certifications with issuer and date.
   - Exclude irrelevant sections or content not related to the job.

2. **Relevance**:
   - Prioritize skills, experiences, and achievements that match the job description.
   - Rearrange or rewrite bullet points to emphasize keywords and phrases from the job description.
   - Remove or minimize irrelevant skills, experiences, or sections that don’t align with the job.

3. **Formatting**:
   - Use simple Markdown syntax (e.g., `#` for headings, `-` for bullet points) to ensure ATS compatibility.
   - Avoid tables, complex formatting, or special characters that might break ATS parsing.
   - Ensure consistent heading levels (e.g., `#` for main sections, `##` for job titles).
   - Use bold (`**`) sparingly for emphasis (e.g., company names or key achievements).

4. **Quantify Achievements**:
   - Where possible, add measurable outcomes (e.g., "Developed a tool that reduced processing time by 25%").
   - If no metrics are provided in the input, infer reasonable ones based on context or rephrase for impact.

5. **Output Requirement**:
   - Return **only the optimized Markdown resume**—no additional text, comments, or explanations.
   - Ensure the Markdown is clean, structured, and ready for direct use in a PDF converter.

### Input:
**Resume (Markdown Format):**
{md_resume}

**Job Description:**
{job_description}

### Output:
Provide the optimized resume in Markdown format with the structure and guidelines above.
"""

def generate_optimized_resume(md_resume: str, job_description: str) -> str:
    """
    Calls the Groq API to generate an optimized resume in Markdown format.

    Args:
        md_resume (str): The user's resume in Markdown format.
        job_description (str): The job description for optimization.

    Returns:
        str: The optimized resume in Markdown format.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")

    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a highly skilled Markdown resume optimizer."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(md_resume=md_resume, job_description=job_description)},
            ],
            model="llama-3.3-70b-versatile",
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise RuntimeError("An error occurred while processing your request") from e

if __name__ == "__main__":
    sample_md_resume = """
    ## Professional Overview
    Software Engineer with experience in Python, Java, and SQL.

    ## Skills
    - Programming Languages: Python, Java
    - Databases: MySQL, PostgreSQL

    ## Experience
    - Software Developer Intern at XYZ Corp.
    """

    sample_job_description = """
    We are seeking a Python Developer with expertise in backend frameworks like Django or Flask.
    Experience with MySQL and REST API development is required.
    """

    optimized_md_resume = generate_optimized_resume(sample_md_resume, sample_job_description)
    print(optimized_md_resume)