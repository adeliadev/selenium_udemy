from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO POR CLASS_NAME =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# retorna elemento pela nome da classe
styled_input = driver.find_elements(By.CLASS_NAME, 'styled-input')

# imprime o valor dos elementos encontrados
for si in styled_input:
    valor = si.get_property('value')
    print(valor)

# retorna elemento que contém ambas as classes, o ponto faz com que o sistema leia como uma única classe
multi_class = driver.find_elements(By.CLASS_NAME, 'styled-input.optional-info')

# imprime o valor dos elementos encontrados
for mc in multi_class:
    valor = mc.get_property('value')
    print(valor)