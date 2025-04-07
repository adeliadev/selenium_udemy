from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/4")
driver.refresh()
driver.find_element(By.ID, 'vantagens')
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.refresh()
# instância do wait, os argumentos sao o driver e o tempo de espera
wait = WebDriverWait(driver=driver, timeout=6)
# espera até o elemento estar presente na tela
wait.until(EC.presence_of_element_located(locator=(By.ID, 'vantagens')))
# tempo entre cada verificação - poll_frequency

driver.refresh()

wait = WebDriverWait(driver=driver, timeout=6, poll_frequency=0.8)

wait.until(EC.presence_of_element_located(locator=(By.ID, 'vantagens')))
# personaliza exception
driver.refresh()

wait = WebDriverWait(driver=driver, timeout=2)

try:
    wait.until(
        method=EC.presence_of_element_located(locator=(By.ID, 'vantagens')),
        message='Não foi encontrado o componente de ID="vantagens"'
    )
except Exception as e:
    print(e.msg)
'''
exemplos:
- lojas com tabelas de produtos
- internet lenta
- alta latência
'''
# se ele verifica a pagina e na mesma hora não acha, ele aguarda o tempo definido em time_to_wait
driver.implicitly_wait(time_to_wait=10)

# o wait é bom pra ser especifico com um elemento da tela
# o implicitly funciona para a página toda e não um elemento especifico