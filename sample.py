from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# Acessa a URL
driver = webdriver.Edge()
driver.get("https://dados.cvm.gov.br/organization/cvm")
wait = WebDriverWait(driver, 15)

# Step 1 - Pesquisa
campo_pesquisa = driver.find_element("id", "field-giant-search")
campo_pesquisa.send_keys("Fundos de Investimento + Documentos + Extrato das Informações")

# Step 2 - Navegacao
botao_pesquisa = driver.find_element("xpath", "//button[@aria-label='Submit' and @value='search']")
botao_pesquisa.click()
sleep(5)

# Step 3 - Navegacao
link_dataset = driver\
    .find_element("css selector", "a[href='/dataset/fi-doc-extrato'][data-format='csv']")
link_dataset.click()
sleep(5)


# Step 4 - Navegacao
link_extrato = driver.\
    find_element("css selector", "a.heading[title='Extratos de Fundos de Investimento (2024)']")
link_extrato.click()
sleep(5)

# Step 5 - Download
link_download = driver.\
    find_element("css selector", "a.btn.btn-primary.resource-url-analytics")
link_download.click()
sleep(5)

# Fecha o navegador
driver.close()
