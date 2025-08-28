import uuid
from helper import extract_data_analysis, read_pdf, get_pdf_paths
from database import AnalyseDatabase
from ai import GroqClient
from models.resums import Resums
from models.file import File

database = AnalyseDatabase()
ai = GroqClient()
job = database.get_job_by_name('Ciência de Dados | Engenheiro de IA Júnior')

cv_path = get_pdf_paths(dir='curriculos')


for path in cv_path:
    content = read_pdf(path)
    print(content)
    resum = ai.resume_cv(content)
    print(resum)
    opnion = ai.generate_opnion(content, job)
    print(opnion)
    score = ai.generate_score(content, job)
    print(score)
    

    resum_schema = Resums(
        id=str(uuid.uuid4()),
        job_id=job.get('id'),
        content=resum,
        file=str(path),
        opnion=opnion
    )

    file_schema = File(
        file_id=str(uuid.uuid4()),
        job_id=job.get('id'),
    )

    analysis_schema = extract_data_analysis(resum, job.get('id'), resum_schema.id, score)

    database.resums.insert(resum_schema.model_dump())
    database.analysis.insert(analysis_schema.model_dump())
    database.files.insert(file_schema.model_dump())


