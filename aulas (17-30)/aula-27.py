from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO PELO DOM =====


driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

'''
- clicando com o botão direito em cima do elemento 
- copiar > copy selector ou xpath
'''

driver.find_elements(By.CSS_SELECTOR, '#social > a:nth-child(2)')