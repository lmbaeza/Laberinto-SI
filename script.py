# Integrantes:
# Oscar Andres Mancera Garzon <oamancerag@unal.edu.co>
# Luis Miguel Baez Aponte <lmbaeza@unal.edu.co>

import time

from selenium import webdriver

from agent import Agent

level = 1

# Aquí se utilizará Chrome
driver = webdriver.Chrome()
 
# URL de la Pagina
URL = 'https://www.juegosinfantilespum.com/laberintos-online/12-auto-buhos.php'

# Abriendo el sitio web
driver.get(URL)

time.sleep(9)

# Obtener el botón por el id
button = driver.find_element_by_id("animation_container")
 
# Click en el botton
button.click()
print("Click")

time.sleep(1)

ask = input("Desea empezar a ejecutar el Bot? [S/N]: ")

if ask == 'S' or ask == 's':
    agent = Agent(driver=driver, level=level)
    agent.percibir()
    agent.pensar()
    agent.actuar()
    agent.close()

# Cerrar el Navegador
driver.close()
