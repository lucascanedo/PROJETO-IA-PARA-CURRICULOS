🤖 Resume Analysis System with AI

This project is a Minimum Viable Product (MVP) of a resume analysis system powered by generative AI.
The goal is to help HR managers compare candidate resumes with a job description and generate a fit analysis, highlighting each candidate’s strengths and weaknesses.

🚀 Features

Upload and analysis of resumes in PDF

Job description registration

Google Drive API integration:
Resumes are automatically stored and retrieved from a Google Drive folder.

Automatic AI-powered analysis:

Fit score for the job.

Key strengths and weaknesses of the candidate.

Streamlit interface, published online with Streamlit Cloud.

Initial database in db.json for MVP data storage.

🛠️ Tech Stack

Python 3.10+

LangChain – AI orchestration.

LLM Models (Groq API / OpenAI) – text analysis.

Streamlit – interactive frontend.

Google Drive API – resume storage and retrieval.

JSON – local database for MVP.

Git/GitHub – version control and publication.

📂 Project Structure
├── ai.py             # Core AI logic
├── analise.py        # Resume vs job description analysis
├── app.py            # Frontend interface (Streamlit)
├── create_job.py     # Job description registration
├── database.py       # Database handling (db.json)
├── download_cv.py    # Google Drive integration
├── helper.py         # Helper functions
├── db.json           # Local database (MVP)
├── pyproject.toml    # Project dependencies
├── README.md         # Documentation
├── MODELS/           # Data model structures
