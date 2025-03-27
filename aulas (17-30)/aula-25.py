from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR XPATH =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# seleção de xpath por caminho absoluto
driver.find_elements(By.XPATH, '/html/body/div/div[2]')

# seleção por tag, // procura em todo o html com a tag
driver.find_elements(By.XPATH, '//input')

# seleção por posição, seleciona input 1 ou 4
driver.find_elements(By.XPATH, '//input[1] | //input[4]')

# seleção por atributo, tem que colocar @ na frente do atributo
driver.find_elements(By.XPATH, '//input[@id="user"]')

# seleção do filho imediato, /tag e para descendente é //tag, ambos depois da primeira tag com //
driver.find_elements(By.XPATH, '//input[@id="user"]/a[1]')