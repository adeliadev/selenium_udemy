from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/2')
# preencher formulários com action chains
email = driver.find_element(By.NAME, 'email')
senha = driver.find_element(By.NAME, 'senha')

# melhor formatação do ActionChains
(
    ActionChains(driver)
    .send_keys_to_element(email, 'contato@gmail.com')
    .send_keys_to_element(senha, '123abc')
    .send_keys_to_element(email, Keys.ENTER)
    .perform()
)

# encadear ações e executar no final
actions = ActionChains(driver)
actions.click(email)
actions.key_down(Keys.CONTROL)
actions.send_keys('a')
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.DELETE)

actions.click(senha)
actions.key_down(Keys.CONTROL)
actions.send_keys('a')
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.DELETE)

actions.perform()