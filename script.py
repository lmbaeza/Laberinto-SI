# Integrantes:
# Oscar Andres Mancera Garzon <oamancerag@unal.edu.co>
# Luis Miguel Baez Aponte <lmbaeza@unal.edu.co>

import time
import random
import inspect

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from screenshot import screen_component_by_id
from image_to_asciify import map_to_ascii

MAP_FILE_NAME = 'map.png'
MAP_ASCII = 'map.txt'


# Aquí se utilizará Chrome
driver = webdriver.Chrome()
 
# URL de la Pagina
URL = 'https://www.juegosinfantilespum.com/laberintos-online/12-auto-buhos.php'

# Abriendo el sitio web
driver.get(URL)

time.sleep(5)

# Obtener el botón por el id
button = driver.find_element_by_id("animation_container")
 
# Click en el botton
button.click()
print("Click")

time.sleep(1)

screen_component_by_id(driver=driver, id_name="animation_container", filename=MAP_FILE_NAME)

map_to_ascii(MAP_FILE_NAME)

# Cargar Mapa es Ascii

mapa = []
with open(MAP_ASCII) as grid:
    mapa = grid.read().split('\n')

# Imprir el mapa en la terminal
for line in mapa:
    print(line)
    
# Lista de Direcciones
DIRECTIONS = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

for i in range(100):
    time.sleep(0.5)
    # Moviemientos aleatorios (Para mostrar la interación con el browser)
    choice = random.choice(DIRECTIONS)
    print("PRESS")
    ActionChains(driver).key_down(choice).perform()
    time.sleep(0.3)
    # stop pressing
    ActionChains(driver).key_up(choice).perform()

driver.close()
