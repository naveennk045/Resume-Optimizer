import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

prompt = """I have a resume formatted in Markdown and a job description.  
Your task is to optimize my resume so it aligns **precisely** with the job requirements.  

### **Guidelines for Optimization:**  
1. **Enhance Relevance**:  
   - Prioritize experiences, skills, and achievements **most relevant** to the job description.  
   - **Remove** or **de-emphasize** irrelevant content.  
2. **Improve Keywords & Formatting**:  
   - Integrate **industry-specific keywords** from the job description where appropriate.  
   - Ensure bullet points highlight measurable achievements.  
3. **Refine Structure & Clarity**:  
   - Keep the formatting **professional, clear, and ATS-friendly**.  
   - Maintain a **concise and impactful** tone.  
4. **Modify Section Order if Necessary**:  
   - If needed, **rearrange sections** (e.g., Skills before Experience) to improve relevance.  
5. **Ensure Markdown Format**:  
   - Output must be **only in Markdown** with **no extra explanations or comments**.  

### **Input Data:**  
**Resume (Markdown Format):**  
{md_resume}  

**Job Description:**  
{job_description}  

### **Output Requirement:**  
Return only the **optimized resume in Markdown format**, strictly following the given guidelines. **Do not include any extra text or explanations.**  
"""


def response(md_resume, job_description):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt.format(md_resume=md_resume, job_description=job_description),
            }
        ],
        model="deepseek-r1-distill-llama-70b",
    )

    return chat_completion.choices[0].message.content