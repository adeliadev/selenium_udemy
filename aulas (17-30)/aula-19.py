from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR ID =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

'''
==== Opções de seleção ====
- ID = "id"
- NAME = "name"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"
'''

# retorna elemento com o id user e pega a propriedade class
driver.find_element(By.ID, 'user').get_property('className')

# find_element() - retorna apenas o primeiro elemento encontrado com o atributo passado
# get_property() - pega a propriedade passada entre ()
nome = driver.find_element(By.ID, 'user').get_property('value')
profissao = driver.find_element(By.ID, 'role').get_property('value')
signo = driver.find_element(By.ID, 'zodiac').get_property('value')
genero = driver.find_element(By.ID, 'gender').get_property('value')

# imprime os valores (value='') dos elementos selecionados por id
print(f'''
    {nome=},
    {profissao=},
    {signo=},
    {genero=}''')


