from solutions.kabum.jobs.step_01_extract import JobExtract
from solutions.kabum.jobs.step_02_transform import JobTransform
from solutions.kabum.jobs.step_03_load import JobLoad
from datetime import datetime

inicio_pipeline = datetime.now()

job_extract = JobExtract("tv")
df_step_01 = job_extract.run_tasks()

job_transform = JobTransform(df_step_01)
df_step_02 = job_transform.run_tasks()

job_load = JobLoad(df_step_02)
df_step_03 = job_load.run_tasks()

tempo_pipeline = datetime.now() - inicio_pipeline

print(f"Tempo de processamento da pipeline: {tempo_pipeline}")

print(df_step_02)
