# 🤖 Sistema de Análise de Currículos com IA

Este projeto é um MVP (Minimum Viable Product) de um sistema de análise de currículos utilizando **IA generativa**.  
O objetivo é ajudar gestores de RH a comparar currículos de candidatos com uma descrição de vaga e gerar uma análise de aderência, destacando os pontos fortes e fracos de cada candidato.

🔗 **Link de acesso**: [curriculo-analyzer.streamlit.app](https://curriculo-analyzer.streamlit.app/)

---

## 🚀 Funcionalidades
- Upload e análise de currículos em PDF  
- Cadastro de descrição de vaga  
- **Integração com Google Drive API**:  
  - Os currículos são armazenados e recuperados automaticamente de uma pasta no Google Drive  
- **Análise automática com IA**:  
  - Pontuação de aderência à vaga  
  - Principais pontos fortes e fracos do candidato  
- **Interface em Streamlit**, publicada online via Streamlit Cloud  
- Banco de dados inicial em `db.json` para armazenar informações do MVP  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**  
- **LangChain** – orquestração da IA  
- **Modelos LLM (Groq API / OpenAI)** – análise de texto  
- **Streamlit** – frontend interativo  
- **Google Drive API** – armazenamento e leitura de currículos  
- **JSON** – banco de dados local para o MVP  
- **Git/GitHub** – versionamento e publicação  

---

## 📂 Estrutura do Projeto

- **ai.py**            # Lógica principal de IA  
- **analise.py**       # Funções de análise de currículos x vaga  
- **app.py**           # Interface frontend (Streamlit)  
- **create_job.py**    # Cadastro de vaga  
- **database.py**      # Manipulação do banco de dados (db.json)  
- **download_cv.py**   # Integração com Google Drive  
- **helper.py**        # Funções auxiliares  
- **db.json**          # Banco de dados local (MVP)  
- **pyproject.toml**   # Dependências do projeto  
- **README.md**        # Documentação (PT-BR)  
- **README-en.md**     # Documentação (EN)  
- **MODELS/**          # Estruturas de banco de dados  

---

## 🔑 Configuração

Para usar a **Google Drive API**, você deve criar um arquivo de credenciais JSON no **Google Cloud** e salvá-lo na raiz do projeto.  
Este arquivo permite que o sistema autentique e acesse os currículos diretamente da pasta do Drive.  

---

## 🌐 Demo

O MVP está publicado no **Streamlit Cloud** e integra com o **Google Drive** para análise de currículos em tempo real.  
