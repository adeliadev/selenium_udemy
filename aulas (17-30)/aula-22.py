from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR LINK_TEXT E PARTIAL_LINK =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# retorna o texto do link que tem o valor passado (<a>texto</a>)
instagram = driver.find_elements(By.LINK_TEXT, 'Instagram')

# partial pega substrings, caracteres dentro de frases/palavras
gram = driver.find_elements(By.PARTIAL_LINK_TEXT, 'gram')

# itera sobre os elementos encontrados
for g in gram:
    valor = g.text
    print(valor)

# seleciona div#social e todos os <a> dela
links = driver.find_element(By.ID, 'social').find_elements(By.TAG_NAME, 'a')

# imprime valores encontrados com 'gram'
for link in links:
    valor = link.text

    if 'gram' in valor:
        print(valor)