# 🤖 AI-Powered Resume Analysis System

This project is an MVP (Minimum Viable Product) of a resume analysis system using generative AI.  
The goal is to help HR managers compare candidate resumes with a job description and generate a match analysis, highlighting each candidate's strengths and weaknesses.  

🔗 Link for access: [curriculo-analyzer.streamlit.app](https://curriculo-analyzer.streamlit.app/)

---

## 🚀 Features
- Upload and analysis of resumes in PDF format.  
- Job description registration.  
- **Google Drive API integration**:  
  Resumes are automatically stored and retrieved from a folder in Google Drive.  
- **AI-powered automatic analysis**:  
  - Match score for the job.  
  - Key strengths and weaknesses of the candidate.  
- **Streamlit interface**, published online via Streamlit Cloud.  
- Initial database in `db.json` to store MVP information.  

---

## 🛠️ Technologies Used
- **Python 3.10+**  
- **LangChain** – AI orchestration.  
- **LLM Models (Groq API / OpenAI)** – text analysis.  
- **Streamlit** – interactive frontend.  
- **Google Drive API** – resume storage and retrieval.  
- **JSON** – local database for MVP.  
- **Git/GitHub** – version control and publishing.  

---

## 📂 Project Structure

- **ai.py**          # Core AI logic
- **analise.py**       # Resume vs job description analysis functions
- **app.py**           # Frontend interface (Streamlit)
- **create_job.py**    # Job description registration
- **database.py**      # Database handler (db.json)
- **download_cv.py**   # Google Drive integration
- **helper.py**        # Utility functions
- **db.json**          # Local database (MVP)
- **pyproject.toml**   # Project dependencies
- **README.md**        # Documentation (PT-BR)
- **README-en.md**     # Documentation (EN)
- **MODELS/**          # Database schema files

---

🔑 Setup Notes

To use Google Drive API, you must create a JSON credentials file from Google Cloud and save it in your project.
This file will allow the system to authenticate and fetch resumes directly from your Drive folder.

---

🌐 Demo

The MVP is deployed on Streamlit Cloud and integrates with Google Drive for real-time resume analysis.,
