from github_extractor.jobs.step_01_extract import JobExtract
import utils.handlers.handler_json as handler


lista_arquivos = handler.get_json_to_list("data/github/files.json")

job_extract = JobExtract(lista_arquivos)
df_step_01 = job_extract.run_tasks()