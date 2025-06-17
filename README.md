
# Resume Ranker – Gemini AI

A smart, prompt-engineered AI app that compares resumes to job descriptions and provides:
-  A match score out of 10  
-  Key matching and missing skills  
-  Final hiring recommendation (Hire / Maybe / Reject)

Built using **Google Gemini 1.5 Flash**, **Gradio**, and **Prompt Engineering** techniques.

---

##  Tech Stack

-  [Google Generative AI (Gemini)](https://ai.google.dev/)
-  Prompt Engineering (Role-aware design)
-  Gradio UI for interaction
-  Environment Variables via `python-dotenv`

---

## Features

- Upload or paste any resume and job description
- Acts like a **real recruiter** using role-based prompting
- Generates structured output:
  - Match Score
  - Matched & Missing Skills
  - Final Verdict

---

##  How It Works

> This app uses **role-aware prompting** to simulate a senior recruiter evaluating a resume.

```txt
Prompt:
You are a senior technical recruiter at Google.
Evaluate this resume against the following Job Description.
