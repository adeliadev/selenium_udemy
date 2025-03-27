from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== ATRIBUTOS E PROPRIEDADES HTML =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/1')

# exemplo de atributo e propriedade que tem o mesmo nome (html e dom)
atr = driver.find_element(By.ID, 'zodiac').get_attribute('id')
prop = driver.find_element(By.ID, 'zodiac').get_property('id')

# exemplo de atributo e propriedade que tem nomes diferentes (html e dom)
atr = driver.find_element(By.ID, 'zodiac').get_attribute('class')
# pode ser visto na aba propriedades do DOM
prop = driver.find_element(By.ID, 'zodiac').get_property('className')

# retorna o valor de data-optional
atr = driver.find_element(By.ID, 'zodiac').get_attribute('data-optional')

# pega tudo que está dentro do dicionário data set e passa exatamente o que quer entre []

prop = driver.find_element(By.ID, 'zodiac').get_property('dataset')['optional']