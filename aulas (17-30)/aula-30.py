from selenium import webdriver
from selenium.webdriver.common.by import By

# ===== SELEÇÃO DE DROPDOWNS =====

driver = webdriver.Chrome()

driver.get('http://localhost:8000/#/exemplo/3')
from selenium.webdriver.support.ui import Select

# seleciona o campo dropdown pelo nome
select = Select(driver.find_element(By.NAME, 'regiao'))

for opt in select.options:
    print(opt.get_attribute('value'), opt.text)

# seleciona pelo indice - começa pelo 0
select.select_by_index(3)

# seleciona pelo texto visivel
select.select_by_visible_text('Goiás')

# seleciona pelo valor (value)
select.select_by_value('0')

# para saber a opção que está selecionada e o seu texto
select.first_selected_option.text

# campo select com multipla seleção
multi = Select(driver.find_element(By.CSS_SELECTOR, '#multi-select select'))

for opt in multi.options:
    print(opt.get_attribute('value'), opt.text)
    
# selecionar mais de um elemento - todas as opções anteriores tambem servem aqui
multi.select_by_index(3)
multi.select_by_visible_text('Goiás')
multi.select_by_value('0')

# retorna todas as opções selecionadas
for opt in multi.all_selected_options:
    print(opt.get_attribute('value'), opt.text)

# para deselecionar em campos de seleção multipla
multi.deselect_by_index(3)
multi.deselect_by_visible_text('Goiás')
multi.deselect_by_value('0')
multi.deselect_all()

# para selecionar a mesma opção em todos os dropdowns (Select)
all_selects = driver.find_elements(By.TAG_NAME, 'select')

for item in all_selects:
    select = Select(item)
    select.select_by_index(2)