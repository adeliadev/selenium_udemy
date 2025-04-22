from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/9')
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').perform()
ActionChains(driver).send_keys(Keys.ALT).perform()
ActionChains(driver).send_keys(Keys.SHIFT).perform()

# funciona como control só que em todas as plataformas
ActionChains(driver).send_keys(Keys.META).perform()

# para atalhos
titulo = driver.find_element(By.CSS_SELECTOR, 'main div.title')
ActionChains(driver).double_click(titulo).click(titulo).perform()

(
    ActionChains(driver)
    .key_down(Keys.META)
    .send_keys('c')
    .key_up(Keys.META)
    .perform()
)