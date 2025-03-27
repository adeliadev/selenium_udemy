from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import json
import time

driver = webdriver.Chrome()

driver.get('https://curso-web-scraping.pages.dev/#/desafio/1')

# leitura do arquivo json
with open('desafio_1.json') as file:
    usuarios = json.load(file)

# fecha sidebar
sidebar = driver.find_element(By.CSS_SELECTOR, '[data-drawer-target="default-sidebar"]')
sidebar.click()

for usuario in usuarios:

    # seleciona email e senha
    email = driver.find_element(By.NAME, 'email')
    senha = driver.find_element(By.NAME, 'senha')

    # limpa campos de email e senha
    email.clear()
    senha.clear()

    # digita email e senha
    email.send_keys(usuario['email'])
    senha.send_keys(usuario['senha'])

    # formata campo data de nascimento do json com datetime
    data = datetime.datetime.strptime(usuario['data-de-nascimento'], '%Y-%m-%d')

    # seleciona os dropdowns de dia, mes e ano
    dia = Select(driver.find_element(By.NAME, 'dia'))
    mes = Select(driver.find_element(By.NAME, 'mes'))
    ano = Select(driver.find_element(By.NAME, 'ano'))

    # envia data para o input por texto visivel - string da variável data
    dia.select_by_visible_text(str(data.day))
    mes.select_by_visible_text(str(data.month))
    ano.select_by_visible_text(str(data.year))

    # seleciona switch da newsletter
    newsletter = driver.find_element(By.ID, 'airplane-mode')
    
    # verifica se o elemento tem o atributo aria-checked ativo
    switch = True if newsletter.get_attribute('aria-checked') == 'true' else False

    # checa se o valor atual do switch é o mesmo do newsletter do json
    if switch != usuario['newsletter']:
        newsletter.click()

    # enviar form
    email.submit()

# tempo pra verificar os cadastros
time.sleep(30)
