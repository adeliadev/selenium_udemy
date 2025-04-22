from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/7')
img = driver.find_element(By.ID, 'imagem_0')

# perform() roda as ações
ActionChains(driver).move_to_element(img).perform()
img = driver.find_element(By.ID, 'imagem_4')

ActionChains(driver).move_to_element(img).perform()

# move_by_offset() move o cursor de acordo com X e Y
ActionChains(driver).move_by_offset(xoffset=140, yoffset=20).perform()

# também aceita valores negativos
ActionChains(driver).move_by_offset(xoffset=-140, yoffset=-120).perform()

# scroll
img = driver.find_element(By.ID, 'imagem_26')

# vai direto pro elemento
ActionChains(driver).scroll_to_element(img).perform()

# o scroll vai de acordo com X e Y
ActionChains(driver).scroll_by_amount(delta_x=0, delta_y=300).perform()

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
img = driver.find_element(By.ID, 'imagem_0')
scroll_origin = ScrollOrigin.from_element(img)

# define onde o scroll começa
ActionChains(driver).scroll_from_origin(scroll_origin=scroll_origin, delta_x=0, delta_y=1000).perform()

# click e double click
driver.get('http:localhost:8000/#/exemplo/8')
proximo = driver.find_element(By.XPATH, '//main//button[contains(text(), "Próxima")]')

ActionChains(driver).click(proximo).perform()
ActionChains(driver).double_click(proximo).perform()