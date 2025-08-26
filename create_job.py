from database import AnalyseDatabase
import uuid
from models.jobs import Job

database = AnalyseDatabase()

name = 'Ciência de Dados | Engenheiro de IA Júnior'

main_activities = '''
Desenvolver e manter pipelines de dados para alimentar modelos de IA (coleta, limpeza, enriquecimento e validação).
Apoiar na implantação de modelos de IA em produção, com foco em escalabilidade, performance e custo.
Monitorar e otimizar modelos em produção, ajustando métricas de performance e robustez.
Colaborar com analistas e cientistas de dados na análise exploratória e geração de insights.
Documentar e versionar os processos e modelos implantados.
Participar da avaliação de novas ferramentas e soluções de IA. 
'''
prerequisities = '''
Formação em Ciência da Computação, Engenharia, Estatística ou áreas correlatas.
Experiência com Python e bibliotecas como Pandas, Scikit-Learn, PyTorch ou TensorFlow.
Conhecimento em bancos de dados (SQL, NoSQL) e ferramentas de visualização (Power BI, Excel).
Vivência com ambientes em nuvem (AWS, Azure) e ferramentas de orquestração (Docker, Kubernetes).
Familiaridade com práticas de DevOps, DataOps ou MLOps.
Desejável experiência com modelos generativos ou LLMs.
Boa capacidade de comunicação e trabalho colaborativo.
'''

differentials = ""

job = Job(
    id= str(uuid.uuid4()),
    name=name,
    main_activities=main_activities,
    prerequisities=prerequisities,
    differentials=differentials
)

database.jobs.insert(job.model_dump())