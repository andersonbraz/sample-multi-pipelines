from github.jobs.step_01_extract import JobExtract
from github.jobs.step_02_transform import JobTransform
from github.jobs.step_03_load import JobLoad
from datetime import datetime

inicio_pipeline = datetime.now()

lista_orgs = ["google", "microsoft", "aws"]
lista_campos = ["id", "name", "full_name", "language", "created_at", "updated_at"]

job_extract = JobExtract(lista_orgs, lista_campos)
df_step_01 = job_extract.run_tasks()

job_transform = JobTransform(df_step_01)
df_step_02 = job_transform.run_tasks()

job_load = JobLoad(df_step_02)
df_step_03 = job_load.run_tasks()

tempo_pipeline = datetime.now() - inicio_pipeline

print(df_step_03)
print(f"Tempo de processamento da pipeline: {tempo_pipeline}")

