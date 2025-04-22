from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()

driver.get("http://localhost:8000/#/exemplo/8")
from io import StringIO

sio = StringIO(initial_value=driver.page_source)

# captura os dados da página e retorna a primeira tabela com o id 'tabela-usuarios'
pd.read_html(io=sio, attrs={'id': 'tabela-usuarios'})[0]