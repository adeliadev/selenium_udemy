from selenium.webdriver.common import utils

# obtem ip de um site
utils.find_connectable_ip(host='google.com')

# retorna porta livre no sistema
utils.free_port()

# testa a conexão de uma porta especifica
utils.is_connectable(port=8000, host='localhost')