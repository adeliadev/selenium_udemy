from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/7")

driver.implicitly_wait(time_to_wait=10)

# seleciona galeria e suas imagens
galeria = driver.find_element(By.ID, 'galeria')
imagens = galeria.find_elements(By.TAG_NAME, 'img')

# mesma coisa só que com uma unica variável
imagens = driver.find_elements(By.CSS_SELECTOR, '#galeria img')
                               
# 
for img in imagens:
    img_src = img.get_property('src')
    img_id = img.get_property('id')
    print(img_id, img_src)

    # cria a pasta se ela ainda não existir
    if not os.path.exists('./imagens'):
        os.mkdir('./imagens')

    # adiciona .jpg no nome da imagem
    file = img_id + '.jpg'
    filename = os.path.join('./imagens', file)

    # recebe a url do arquivo e o nome do arquivo
    urllib.request.urlretrieve(img_src, filename)