from selenium import webdriver

# ===== PROPRIEDADES DO DRIVER =====

# instância do driver
driver = webdriver.Chrome()

# abre a url que está entre os ()
driver.get('https://google.com')

# retorna titulo da página
driver.title

# retorna a url atual do navegador
driver.current_url

# deixa o navegador em tela cheia
driver.fullscreen_window()

# pega informações sobre o navegador (XY)
driver.get_window_rect()

# decide o X e Y da janela do navegador
driver.set_window_rect(x=300, y=300)

# maximiza a janela
driver.maximize_window()

# minimiza a janela
driver.minimize_window()

# retorna o nome do navegador (driver) que está sendo executado
driver.name

# retorna todo o conteudo html da página que esta sendo executada
driver.page_source

# atualiza a página
driver.refresh()

# abre outra url
driver.get('https://youtube.com')

# volta à página anterior
driver.back()

# vai para a próxima página (se tiver)
driver.forward()

# encerra o driver
driver.quit()