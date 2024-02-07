from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Acessa a URL
driver = webdriver.Edge()
driver.get("https://dados.cvm.gov.br/organization/cvm")

# Espera o carregamento da página
sleep(5)

# Localiza o campo de pesquisa
campo_pesquisa = driver.find_element(By.ID, "field-giant-search")

# Preenche o campo de pesquisa
campo_pesquisa.send_keys("Fundos de Investimento + Documentos + Extrato das Informações")

# Localiza o botão de pesquisa
botao_pesquisa = driver.find_element(By.XPATH, "//button[@aria-label='Submit' and @value='search']")

# Clica no botão de pesquisa
botao_pesquisa.click()

# Espera o resultado da pesquisa
sleep(5)

link_dataset = driver.find_element(By.CSS_SELECTOR, "a[href='/dataset/fi-doc-extrato'][data-format='csv']")

# Clica no link do dataset
link_dataset.click()

sleep(5)

# Localiza o link para o extrato de fundos de investimento
link_extrato = driver.find_element(By.CSS_SELECTOR, "a.heading[title='Extratos de Fundos de Investimento (2024)']")

# Clica no link do extrato
link_extrato.click()

sleep(15)

# Fecha o navegador
driver.close()
