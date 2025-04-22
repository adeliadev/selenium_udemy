from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from dataclasses import dataclass, asdict
import json

driver = webdriver.Chrome()

driver.get('http:localhost:8000/#/desafio/4')

# define as propriedades dos cards de produtos
@dataclass
class Produto:
    titulo: str
    e_frete_gratis: bool
    e_parcelamento_sem_juros: bool
    e_envio_internacional: bool
    esta_em_oferta: bool
    numero_estrelas: int
    descricao: str
    foto: str
    preco: float

# tempo de espera pelos componentes
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
driver.implicitly_wait(time_to_wait=10)
def acessar_produtos(categoria: str):
    # para garantir que está na página correta
    driver.get('http://localhost:8000/#/desafio/4')

    # seleciona a categoria
    (
        ActionChains(driver)
        .click(driver.find_element(By.XPATH, f'//h1[contains(text(), "{categoria}")]'))
        .perform()
    )
def capturar_dados_dos_produtos(): # ERRO AQUI
    dados = []

    while True:
        # Aguarde até que os produtos estejam visíveis
        wait.until(EC.visibility_of_all_elements_located(
            locator=(By.CSS_SELECTOR, 'form#filtros + div > div > img')
        ))

        produtos = driver.find_elements(By.CSS_SELECTOR, 'form#filtros + div div:has(>img)')

        for produto in produtos:
            # Coleta dados do produto
            titulo = produto.find_element(By.TAG_NAME, 'h5').text
            descricao = produto.find_element(By.TAG_NAME, 'p').text
            foto = produto.find_element(By.TAG_NAME, 'img').get_attribute('src')
            preco = produto.find_element(By.CSS_SELECTOR, 'div:has(>span:nth-last-child(2)) > span:nth-child(2)').text

            # Verificação de frete grátis, parcelamento sem juros, envio internacional e em oferta
            e_frete_gratis = bool(produto.find_elements(By.CSS_SELECTOR, 'div.bg-blue-100'))
            e_parcelamento_sem_juros = bool(produto.find_elements(By.CSS_SELECTOR, 'div.bg-green-100'))
            e_envio_internacional = bool(produto.find_elements(By.CSS_SELECTOR, 'div.bg-orange-100'))
            esta_em_oferta = bool(produto.find_elements(By.CSS_SELECTOR, 'div.bg-purple-100'))

            # Número de estrelas
            numero_estrelas = len(produto.find_elements(By.CSS_SELECTOR, 'svg.text-yellow-300'))

            # Cria a instância de Produto e adiciona ao resultado
            dados_do_produto = Produto(
                titulo=titulo,
                e_frete_gratis=e_frete_gratis,
                e_parcelamento_sem_juros=e_parcelamento_sem_juros,
                e_envio_internacional=e_envio_internacional,
                esta_em_oferta=esta_em_oferta,
                numero_estrelas=numero_estrelas,
                descricao=descricao,
                foto=foto,
                preco=preco
            )

            dados.append(dados_do_produto)

        try:
            # Tente clicar no botão "próximo" e vá para a próxima página
            proximo = driver.find_element(By.CSS_SELECTOR, 'form#filtros + div button:last-child')
            proximo.click()
        except Exception as e:
            # Se não houver mais página, saia do loop e registre a exceção para depuração
            print(f"Erro ao clicar no botão 'próximo': {e}")
            break
            
    return dados

def preencher_filtros(
    frete_gratis = bool,
    parcelamento_sem_juros = bool,
    envio_internacional = bool,
    em_oferta = bool,
    preco_minimo = int,
    preco_maximo = int,
    nota = int  
):
    # Modificar - filtros
    frete = driver.find_element(By.ID, 'frete')
    parcelamento = driver.find_element(By.ID, 'parcelamento')
    internacional = driver.find_element(By.ID, 'envio-internacional')
    oferta = driver.find_element(By.ID, 'oferta')

    # preços
    preco_de = driver.find_element(By.ID, 'price-from')
    preco_ate = driver.find_element(By.ID, 'price-to')

    # classificação
    nota5 = driver.find_element(By.ID, 'five-stars')
    nota4 = driver.find_element(By.ID, 'four-stars')
    nota3 = driver.find_element(By.ID, 'three-stars')
    nota2 = driver.find_element(By.ID, 'two-stars')
    nota1 = driver.find_element(By.ID, 'one-star')

    # botoes
    buscar = driver.find_element(By.CSS_SELECTOR, 'form#filtros button[type="submit"]')
    limpar = driver.find_element(By.CSS_SELECTOR, 'form#filtros button[type="reset"]')

    actions = ActionChains(driver)
    actions.click(limpar).perform()

    if frete_gratis:
        actions.click(frete)
    if parcelamento_sem_juros:
        actions.click(parcelamento)
    if envio_internacional:
        actions.click(internacional)
    if em_oferta:
        actions.click(oferta)

    # limpa campos de preço
    preco_de.clear()
    preco_ate.clear()

    # envia valores para o campo
    actions.send_keys_to_element(preco_de, preco_minimo)
    actions.send_keys_to_element(preco_ate, preco_maximo)

    # checa as classificações
    match nota:
        case 5:
            actions.click(nota5)
        case 4:
            actions.click(nota4)
        case 3:
            actions.click(nota3)
        case 2:
            actions.click(nota2)
        case 1:
            actions.click(nota1)
            
    actions.click(buscar)
    actions.perform()

# Selecionar todos os produtos da categoria Celulares com frete grátis, em oferta, preço entre R$ 500 e R$ 2.500 reais e com 4 estrelas.
acessar_produtos(categoria='Celulares')
preencher_filtros(
    frete_gratis = True,
    parcelamento_sem_juros = False, 
    envio_internacional = False,
    em_oferta = True,
    preco_minimo = 500,
    preco_maximo = 2500,
    nota = 4
)
celulares = capturar_dados_dos_produtos()
celulares
# Selecionar todos os produtos da categoria TVs com envio internacional, preço até R$ 5.000 e 5 estrelas.
acessar_produtos(categoria='TVs')

preencher_filtros(
    frete_gratis = False,
    parcelamento_sem_juros = False, 
    envio_internacional = True,
    em_oferta = True,
    preco_minimo = 1,
    preco_maximo = 5000,
    nota = 5
)

tvs = capturar_dados_dos_produtos()
tvs
# Selecionar todos os produtos da categoria Games com parcelamento sem juros, frete grátis, preço entre R$ 2.000 e R$ 8.000 reais e 3 estrelas.
acessar_produtos(categoria='Games')

preencher_filtros(
    frete_gratis = True,
    parcelamento_sem_juros = True, 
    envio_internacional = False,
    em_oferta = False,
    preco_minimo = 2000,
    preco_maximo = 8000,
    nota = 3
)

games = capturar_dados_dos_produtos()
games
# Selecionar todos os produtos da categoria Notebooks com parcelamento sem juros, em oferta, preço entre R$ 1.234 e R$ 7.896 reais e 4 estrelas.
acessar_produtos(categoria='Notebooks')

preencher_filtros(
    frete_gratis = False,
    parcelamento_sem_juros = True, 
    envio_internacional = False,
    em_oferta = True,
    preco_minimo = 1234,
    preco_maximo = 7896,
    nota = 4
)

notebooks = capturar_dados_dos_produtos()
notebooks

# Exportar todos os dados coletados para um JSON e um CSV. 
todos_os_produtos = celulares + tvs + games + notebooks

l = [1,2]
l.extend([3,4])

with open('desafio_exp.json', 'w') as file:
    dados_formatados = [asdict(d) for d in todos_os_produtos]
    json.dump(dados_formatados, file, ensure_ascii=False)