from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR CSS_SELECTOR =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

'''
===== Opções =====
- hashtag (#) -> seletor de id
- . -> seletor de classe
- seta direita (>) -> seletor de filhos diretos
- ~ -> seletor de irmãos
- + -> seletor de irmão imediato
- * seletor de todos os elementos
- [property='value'] -> seletor de propriedades
    - ^= -> corresponde a um prefixo (começam com)
    - $= -> corresponde a um sufixo (terminam com)
    - *= -> corresponde a uma substring
    - |= -> corresponde a um texto seguido por hífen
    - ~= -> corresponde a uma palavra
'''

# seleção por id, seleciona uma div com o id
driver.find_element(By.CSS_SELECTOR, 'div#social')

# seleção por classe, seleciona inputs com a classe 
driver.find_elements(By.CSS_SELECTOR, 'input.styled-input.optional-info')

# seleção por parentesco
driver.find_elements(By.CSS_SELECTOR, 'div.main-container input.optional-info')

# seleção por filho direto
driver.find_elements(By.CSS_SELECTOR, 'div#social > a')

# retorna todos os descendentes da tag main
driver.find_elements(By.CSS_SELECTOR, 'div.main-container *')

# retorna todos os filhos diretos da div
main_container = driver.find_elements(By.CSS_SELECTOR, 'div#social > *')

# imprime o nome da tag e suas classes
for mc in main_container:
    print(mc.tag_name, '=>', mc.get_property('className'))

# seleção por propriedade
driver.find_elements(By.CSS_SELECTOR, 'input[name="fullname"]')

# selecionando duas propriedades, não pode ter espaço entre os []
driver.find_elements(By.CSS_SELECTOR, 'input[disabled][data-optional="true"]')

# seleção de propiedade por sufixo com $=
driver.find_elements(By.CSS_SELECTOR, 'input[value$="ino"]')

# seleção por prefixo indenpendente da tag
driver.find_elements(By.CSS_SELECTOR, '[name^="user"]')

# seleção toda palavra que é seguida por hífen usando |=
driver.find_elements(By.CSS_SELECTOR, '[class|="text"]')

# seleção por substring usando *=
driver.find_elements(By.CSS_SELECTOR, 'input[id*="e"]')