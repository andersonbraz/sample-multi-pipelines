from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://github.com/MicrosoftLearning/DP100/blob/master/data/diabetes.csv'


def main():
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(15)

    # Seleciona o botão de download
    download_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Download raw content')]")

    # Obtém o valor do atributo `href` do botão
    download_url = download_button.get_attribute('href')
    print("------------------ Url: ", download_url)

    # # Abre o arquivo
    # with open(download_url, 'wb') as f:
    #     f.write(driver.get(download_url).content)

    # Aguarda o download do arquivo ser concluído
    time.sleep(15)
    driver.close()


if __name__ == '__main__':
    main()
