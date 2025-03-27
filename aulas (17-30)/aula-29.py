from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ===== PREENCHIMENTO DE FORMULÁRIOS =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/2')

# variáveis com os elementos selecionados
email = driver.find_element(By.NAME, 'email')
senha =  driver.find_element(By.NAME, 'senha')
enviar = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

# escreve email e senha
email.send_keys('teste@xyz.com')
senha.send_keys('123abc')

# clica no botão
enviar.click()

# para limpar o campo antes de escrever outra coisa
email.clear()
senha.clear()

# envia novo email para o input
email.send_keys("selenium@xyz.com")
senha.send_keys("123")
enviar.click()

# para limpar o campo antes de escrever outra coisa
email.clear()
senha.clear()

# envia novo email para o input
email.send_keys("selenium@xyz.com")
senha.send_keys("123")

# substitui ter que selecionar o botão diretamente para enviar o formulário - MAIS USADA
email.submit()

# para limpar o campo antes de escrever outra coisa
email.clear()
senha.clear()

# envia novo email para o input
email.send_keys("selenium@xyz.com")
senha.send_keys("123")

# outra forma de substituir sem selecionar o botão diretamente
email.send_keys(Keys.ENTER)