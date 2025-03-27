from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR NAME =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# seleciona informações do usuário por name=''
nome = driver.find_element(By.NAME, 'fullname').get_property('value')
profissao = driver.find_element(By.NAME, 'role').get_property('value')
signo = driver.find_element(By.NAME, 'zodiacSign').get_property('value')
genero = driver.find_element(By.NAME, 'genderOfBirth').get_property('value')

# imprime os valores (value="") das variáveis anteriores
print(f'''
    {nome=},
    {profissao=},
    {signo=},
    {genero=}''')

