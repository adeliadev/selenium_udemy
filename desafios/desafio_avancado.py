from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/desafio/2")

driver.implicitly_wait(time_to_wait=10)

@dataclass
class Usuario:
    foto: str
    nome: str
    profissao: str
    email: str
    telefone: str
    perfil: str
    estado: str

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.new_window('tab')
driver.get("http://localhost:8000/#/desafio/3")

windows = {
    'busca': driver.window_handles[0],
    'cadastro': driver.window_handles[1]
}
while True:
    driver.switch_to.window(window_name=windows['cadastro'])

    try:
        usuario_busca = driver.find_element(By.ID, 'usuario').text
    except:
        break

    
    driver.switch_to.window(window_name=windows['busca'])

    busca = driver.find_element(By.CSS_SELECTOR, 'main input[type="text"]')
    busca.clear()
    busca.send_keys(usuario_busca)
    enviar = driver.find_element(By.CSS_SELECTOR, 'main button')

    dados = []

    wait = WebDriverWait(driver=driver, timeout=30, poll_frequency=1)
    wait.until(EC.element_to_be_clickable(mark=enviar))
    enviar.click()

    # espera até as imagens estarem carregadas
    wait.until(EC.visibility_of_all_elements_located(locator=(By.CSS_SELECTOR, 'div.users-list > div > img')))
    users = driver.find_elements(By.CSS_SELECTOR, 'div.users-list > div')

    for user in users:
        # captura os dados dos usuários
        foto = user.find_element(By.TAG_NAME, 'img')
        nome = user.find_element(By.TAG_NAME, 'h3')
        profissao = user.find_element(By.TAG_NAME, 'span')
        email = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(1)')
        telefone = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(2)')
        perfil = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(3)')
        estado = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(4)')

        # formata para salvar na variável dos dados
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

    driver.switch_to.window(window_name=windows['cadastro'])


    nome_cadastro = driver.find_element(By.NAME, 'nome')
    profissao_cadastro = driver.find_element(By.NAME, 'profissao')
    email_cadastro = driver.find_element(By.NAME, 'email')
    telefone_cadastro = driver.find_element(By.NAME, 'telefone')
    perfil_cadastro = driver.find_element(By.NAME, 'usuario')
    estado_cadastro = Select(driver.find_element(By.NAME, 'estado'))

    for dt in dados:

        nome_cadastro.clear()
        profissao_cadastro.clear()
        email_cadastro.clear()
        telefone_cadastro.clear()
        perfil_cadastro.clear()

        nome_cadastro.send_keys(dt.nome)
        profissao_cadastro.send_keys(dt.profissao)
        email_cadastro.send_keys(dt.email)
        telefone_cadastro.send_keys(dt.telefone)
        perfil_cadastro.send_keys(dt.perfil)
        estado_cadastro.select_by_visible_text(dt.estado)

        nome_cadastro.submit()