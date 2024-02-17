from solutions.cvm.jobs.step_01_extract import JobExtract
import utils.handlers.handler_json as handler

lista_navegacao = handler.get_json_to_list("data/cvm/navigation_cvm_fi.json")

job_extract = JobExtract(lista_navegacao)
df_step_01 = job_extract.run_tasks()
