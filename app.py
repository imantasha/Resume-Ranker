import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Resume Ranker Logic
def rank_resume(resume, jd):
    prompt = f"""
You are a senior technical recruiter at Google.

Evaluate the following resume against the provided Job Description.

Provide:
1. Match score out of 10
2. Key matching skills
3. Missing skills
4. Recommendation (Hire / Maybe / Reject)

Resume:
{resume}

Job Description:
{jd}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f" Error: {e}"

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("##  Resume Ranker - Gemini AI")
    gr.Markdown("Paste your Resume and Job Description below to get match analysis.")
    
    with gr.Row():
        resume_input = gr.Textbox(lines=15, label=" Resume (Paste text)")
        jd_input = gr.Textbox(lines=15, label="Job Description (Paste JD)")

    output = gr.Textbox(label=" Result")
    btn = gr.Button(" Rank Resume")
    btn.click(rank_resume, inputs=[resume_input, jd_input], outputs=output)

if __name__ == "__main__":
    app.launch()
