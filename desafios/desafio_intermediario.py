from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Chrome()
driver.get('http://localhost:8000/#/desafio/2')

'''
1 - buscar usuários lendo o json
2 - esperar retornar os dados
3 - capturar informações do usuários
4 - salvar informações em json e csv
'''

driver.refresh()

from dataclasses import dataclass

# classe ajuda a estruturar caso precise colocar num bd, por exemplo

@dataclass
class Usuario:
    foto: str
    nome: str
    profissao: str
    email: str
    telefone: str
    perfil: str
    estado: str

# seleciona o input de busca e o botao de pesquisar
busca = driver.find_element(By.CSS_SELECTOR, 'main input[type="text"]')
enviar = driver.find_element(By.CSS_SELECTOR, 'main button')

with open('./desafios/desafio_2.json') as file:
    usuarios = json.load(file)

# lista vazia para guardar os dados
dados = []

for usuario in usuarios:
    # busca informação do json
    busca.clear()
    busca.send_keys(usuario)

    # aguarda o botão ficar clicável para buscar
    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
    wait.until(EC.element_to_be_clickable(mark=enviar))
    enviar.click()

    wait.until(EC.visibility_of_all_elements_located(locator=(By.CSS_SELECTOR, 'div.users-list > div > img')))
    users = driver.find_elements(By.CSS_SELECTOR, 'div.users-list > div')

    for user in users:
        foto = user.find_element(By.TAG_NAME, 'img')
        nome = user.find_element(By.TAG_NAME, 'h3')
        profissao = user.find_element(By.TAG_NAME, 'span')
        email = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(1)')
        telefone = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(2)')
        perfil = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(3)')
        estado = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(4)')

        dados_do_usuario = Usuario(
            foto =  foto.get_attribute('src'),
            nome = nome.text,
            profissao = profissao.text,
            email = email.text[8:],
            telefone = telefone.text[10:],
            perfil = perfil.text[9:],
            estado = estado.text[8:]
        )

        dados.append(dados_do_usuario)

print(dados)

# salvar em json
from dataclasses import asdict

# se o arquivo não existir, será criado
with open('./desafios/dados_capturados.json', 'w', encoding='utf-8') as file:
    dado_formatado = [asdict(d) for d in dados]
    json.dump(dado_formatado, file, ensure_ascii=False)

# salvar em csv
import csv
from dataclasses import fields

with open('./desafios/dados_capturados.csv', 'w', newline='', encoding='utf-8') as csvfile:
    headers = [field.name for field in fields(Usuario)]
    file = csv.DictWriter(csvfile, fieldnames=headers)

    file.writeheader()

    dado_formatado = [asdict(d) for d in dados]
    file.writerows(dado_formatado)