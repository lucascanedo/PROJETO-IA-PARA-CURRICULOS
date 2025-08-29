# 🤖 Sistema de Análise de Currículos com IA

Este projeto é um **MVP (Minimum Viable Product)** de um sistema de análise de currículos utilizando **IA generativa**.  
O objetivo é auxiliar **gestores de RH** a comparar currículos de candidatos com uma **descrição de vaga** e gerar uma análise de aderência, destacando pontos fortes e fracos de cada candidato.

---

## 🚀 Funcionalidades

- Upload e análise de currículos em **PDF**.
- Cadastro de descrição de vaga.
- Integração com **Google Drive API**:
  - Os currículos são armazenados e recuperados automaticamente de uma pasta no Google Drive.
- Análise automática com IA:
  - Pontuação de aderência à vaga.
  - Principais pontos fortes e fracos do candidato.
- Interface em **Streamlit**, publicada online no **Streamlit Cloud**.
- Banco de dados inicial em `db.json` para armazenar informações do MVP.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **LangChain** – orquestração da IA.
- **Modelos LLM (Groq API / OpenAI)** – análise de texto.
- **Streamlit** – frontend interativo.
- **Google Drive API** – armazenamento e leitura de currículos.
- **JSON** – banco de dados local no MVP.
- **Git/GitHub** – versionamento e publicação.

---

## 📂 Estrutura do Projeto

├── ai.py # Lógica principal de IA
├── analise.py # Funções de análise de currículos x vaga
├── app.py # Interface frontend (Streamlit)
├── create_job.py # Cadastro de vaga
├── database.py # Manipulação do banco de dados (db.json)
├── download_cv.py # Função para integração com Google Drive
├── helper.py # Funções auxiliares
├── db.json # Banco de dados local (MVP)
├── pyproject.toml # Dependências do projeto
├── README.md # Documentação
├──MODELS # Pasta com as estruturas dos bancos de dados
