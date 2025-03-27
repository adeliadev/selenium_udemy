from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR TAG_NAME =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# find_elements() retorna todos os elementos com o valor passado entre ()
campos = driver.find_elements(By.TAG_NAME, 'input')

# usa loop para iterar sobre a lista de elementos e imprimir o valor de cada uma
for campo in campos:
    valor = campo.get_property('value')
    print(valor)

# seleciona todas as tags <span>
redes_sociais = driver.find_elements(By.TAG_NAME, 'span')


# .text pega o texto que fica entre a tag <tag>texto<tag>
for rede in redes_sociais:
    valor = rede.text
    print(valor)

# pega div#social e todos os <span> dentro dela (concatenação de busca)
# seleciona primeiro uma div e depois retorna os spans dela
redes_sociais = driver.find_element(By.ID, 'social').find_elements(By.TAG_NAME, 'span')

for rede in redes_sociais:
    valor = rede.get_property('innerText')
    print(valor)