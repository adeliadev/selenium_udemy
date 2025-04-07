from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/5")
wait = WebDriverWait(driver=driver, timeout=30, poll_frequency=1)
# aguarda ate o titulo ser o valor passado em title=""
# %time retorna o tempo de execução
driver.refresh()
%time wait.until(EC.title_is(title='Programador'))
# espera o titulo conter o valor passado em title=""
driver.refresh()
%time wait.until(EC.title_contains(title='Aventureiro'))
# espera elemento passado em locator="" ficar presente na tela
driver.refresh()
%time wait.until(EC.presence_of_element_located(locator=(By.ID, 'star1')))
# retorna o primeiro elemento encontrado
driver.refresh()
%time wait.until(EC.presence_of_all_elements_located(locator=(By.NAME, 'stars')))
# checa se já está disponível no html
driver.refresh()
%time wait.until(EC.visibility_of_element_located(locator=(By.ID, 'star3')))
# checa se o elemento já está clicável
driver.refresh()
%time wait.until(EC.element_to_be_clickable(mark=(By.ID, 'telegram')))
# espera até que um elemento não esteja mais presente na página
driver.refresh()
star = driver.find_element(By.ID, 'star4')
%time wait.until(EC.staleness_of(element=star))
# espera até que o elemento tenha uma propriedade especifica
# %%time deixa você quebrar linha, já %time não
%%time
driver.refresh()
wait.until(EC.element_attribute_to_include(
    locator=(By.ID, 'star5'), 
    attribute_='name'
))

# presence_of_element_located
# element_to_be_clickable
# mais usados
# espera ate que um pop-up apareça
driver.refresh()
%time wait.until(EC.alert_is_present())