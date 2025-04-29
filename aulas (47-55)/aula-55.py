from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/11')

# tipos de log disponíveis
driver.log_types

# retorna as logs desse tipo presentes no console
driver.get_log('browser')
driver.get_log('driver')

# execução com js no devtools
driver.execute_script('return document.title')

driver.execute_script("""
Array(30).fill(0).map((_, index) => console.error(`Erro ${index} encontrado!`))
""")