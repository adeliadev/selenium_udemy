from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/1")
# salva screenshot na pasta
driver.save_screenshot(filename='./screenshots/0.png')
driver.get_screenshot_as_file(filename='./screenshots/1.png')

# para obter os dados do png e pegar os dados para criar a foto na pasta

with open('./screenshots/2.png', 'wb') as file:
    dados = driver.get_screenshot_as_png()
    file.write(dados)
main = driver.find_element(By.TAG_NAME, 'main')
# tira screenshot do elemento selecionado
main.screenshot(filename='./screenshots/3.png')
social = driver.find_element(By.ID, 'social')
social.screenshot(filename='./screenshots/4.png')

import base64
### salvar em pdf

with open('./screenshots/foto.pdf', 'wb') as file:
    dados = driver.print_page()
    converter = base64.b64decode(dados)
    file.write(converter)