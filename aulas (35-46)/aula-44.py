from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/1")
# mostra as guias abertas
driver.window_handles
# mudar de guia utilizando o id que o selenium gera
driver.switch_to.window(window_name='1B035D27BFD423A6D8AD5B96611696FB')
windows = {
    'Exemplo 1': '30A1BF59D7A85E68C73C5789080E2DDA',
    'Exemplo 2': '52769A90B77D5A0238FF8AFDEC2564C4',
    'Exemplo 3': '956DE14BF95242C7EF462A6CA280C472',
    'Exemplo 4': '95273BFC0559D73CA89C3D7FDC913102'
}
# se mudar manualmente após o driver mudar, ele fica na mesma do comando
driver.switch_to.window(window_name=windows['Exemplo 3'])

# cria nova guia
driver.switch_to.new_window('tab')
driver.get('http://google.com.br')
# cria nova janela
driver.switch_to.new_window('window')

# acessa sem ter que nomear as guias em dicionarios ou coisas do tipo
driver.switch_to.window(window_name=driver.window_handles[2])
# pega url da guia ativa no momento
driver.current_url
driver.switch_to.new_window('tab')

driver.get("http://localhost:8000/#/exemplo/5")

driver.find_element(By.CSS_SELECTOR, 'main button.btn-primary').click()

# alerta do navegador
alerta = driver.switch_to.alert
alerta.text

# para cancelar e aceitar no alert
alerta.dismiss()
alerta.accept()
alerta.send_keys('para alerta que pode digitar')