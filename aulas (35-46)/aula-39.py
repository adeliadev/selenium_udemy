from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/6")

driver.implicitly_wait(time_to_wait=10)
# seleciona div e para obter suas propriedades
estados = driver.find_element(By.ID, 'estados')
## ATRIBUTOS
estados.get_attribute('class')
estados.get_attribute('id')

### PROPRIEDADES
estados.get_property('className')
estados.get_property('id')
# 'children' busca os filhos diretos do elemento, mesmo que #estados > div
children = estados.get_property('children')

for child in children:
    cchild = child.get_property('children')
    for cc in cchild:
        if cc.tag_name == 'label':
            print(cc.text)

        # o que for div terá tab e -
        if cc.tag_name == 'div':
            print('\t -', cc.text)
# dataset serve para todas as propriedades que começam com data-
estados.get_property('dataset')['country']
# retorna todo o html do elemento selecionado
estados.get_property('outerHTML')
### size, location, rect, value of css
estados.size
# localização do componente na página
estados.location
# mostra tamanho e localização
estados.rect
# mostra o valor da propriedade css do elemento selecionado
estados.value_of_css_property('border-bottom-style')
estados.value_of_css_property('font-weight')

print(estados.tag_name)

for estado in estados.get_property('children'):
    print(' -', estado.tag_name)