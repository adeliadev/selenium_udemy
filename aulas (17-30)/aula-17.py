from selenium import webdriver

# ===== CONFIGURAÇÕES DO DRIVER =====

# instância do driver
driver = webdriver.Chrome()

# get() para abrir links/sites
driver.get('https://google.com')