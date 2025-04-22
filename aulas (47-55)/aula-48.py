from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('http:localhost:8000/#/exemplo/8')

proximo = driver.find_element(By.XPATH, '//main//button[contains(text(), "Próxima")]')

# pause() - entre os parenteses ficam os segundos que ele vai ficar pausado
ActionChains(driver).click(proximo).pause(5).click(proximo).perform()

# click_and_hold() - clica e segura o botao e release() - solta o botao
ActionChains(driver).click_and_hold(proximo).pause(5).release(proximo).perform()

# drag_and_drop() - arrasta e solta o elemento selecionado
driver.get('http://localhost:8000/#/exemplo/9')

componente_origem = driver.find_element(By.ID, 'drag-source')
componente_destino = driver.find_element(By.ID, 'drag-target')

# tem source e target que são "origem" e "alvo"
ActionChains(driver).drag_and_drop(source=componente_origem, target=componente_destino).perform()

# context_click() - abre o menu com o botão direito
img = driver.find_element(By.ID, 'main-image')
ActionChains(driver).context_click(img).perform()

# Keys - pressiona teclas
ActionChains(driver).send_keys(Keys.TAB).perform()

# segurar tecla (key down) e solta (key up)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

titulo = driver.find_element(By.CSS_SELECTOR, 'main div.title')

# seleciona o titulo
ActionChains(driver).double_click(titulo).click(titulo).perform()

# copia o texto do titulo
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

from pandas.io.clipboard import clipboard_set, clipboard_get
clipboard_get()
clipboard_set('novo texto copiado')
clipboard_get()
import clipboard

# lib mais leve que o pandas e faz a mesma coisa
clipboard.paste()