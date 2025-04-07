from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/8")

driver.implicitly_wait(time_to_wait=10)
# seleciona a tabela
tabela = driver.find_element(By.ID, 'tabela-usuarios')
# seleciona as linhas da tabela
linhas = tabela.find_elements(By.CSS_SELECTOR, 'tbody tr')
from dataclasses import dataclass

@dataclass
class Usuario:
    avatar: str
    nome: str
    profissao: str
    email: str
    perfil: str
    estado: str
registros = []

for linha in linhas:
    dados = linha.get_property('children')

    registro = Usuario(
        avatar = dados[0].find_element(By.TAG_NAME, 'img').get_property('src'),
        nome = dados[1].text,
        profissao = dados[2].text,
        email = dados[3].text,
        perfil = dados[4].text,
        estado = dados[5].text,
    )

    registros.append(registro)
proximo = driver.find_element(By.XPATH, '//main//button[contains(text(), "Próxima")]')

def raspar_dados_da_tabela():
    linhas = tabela.find_elements(By.CSS_SELECTOR, '#tabela-usuarios tbody tr')

    
    registros = []

    for linha in linhas:
        dados = linha.get_property('children')

        registro = Usuario(
            avatar = dados[0].find_element(By.TAG_NAME, 'img').get_property('src'),
            nome = dados[1].text,
            profissao = dados[2].text,
            email = dados[3].text,
            perfil = dados[4].text,
            estado = dados[5].text,
        )

        registros.append(registro)

    return registros
    
dados_da_tabela = []

while True:
    dados = raspar_dados_da_tabela()
    dados_da_tabela.extend(dados)

    try:
        proximo = driver.find_element(By.XPATH, '//main//button[contains(text(), "Próxima")]')
        proximo.click()
    except Exception as e:
        break
len(dados_da_tabela)