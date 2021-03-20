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
from image_map_processing import run_map_processing
from get_path import get_path

level = 1

MAP_FILE_NAME = 'img/map-' + str(level) + '.png'
SERIALIZED_MAP_PATH = 'img/serialized-map.png'
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

# Tomar screemshot del mapa
screen_component_by_id(driver=driver, id_name="animation_container", filename=MAP_FILE_NAME)

# Procesar la Imagen
run_map_processing(level=level)

path = get_path()

print('path : ', path)

# Lista de Direcciones
DIRECTIONS = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

for direction in path:
    time.sleep(0.5)

    milliseconds = 0.085

    if direction == 'U':
        # Selecionar Tecla
        ActionChains(driver).key_down(DIRECTIONS[0]).perform()
        time.sleep(milliseconds)
        # Parar Seleción
        ActionChains(driver).key_up(DIRECTIONS[0]).perform()
    elif direction == 'D':
        # Selecionar Tecla
        ActionChains(driver).key_down(DIRECTIONS[1]).perform()
        time.sleep(milliseconds)
        # Parar Seleción
        ActionChains(driver).key_up(DIRECTIONS[1]).perform()
    elif direction == 'L':
        # Selecionar Tecla
        ActionChains(driver).key_down(DIRECTIONS[2]).perform()
        time.sleep(milliseconds)
        # Parar Seleción
        ActionChains(driver).key_up(DIRECTIONS[2]).perform()
    elif direction == 'R':
        # Selecionar Tecla
        ActionChains(driver).key_down(DIRECTIONS[3]).perform()
        time.sleep(milliseconds)
        # Parar Seleción
        ActionChains(driver).key_up(DIRECTIONS[3]).perform()

# Cerrar el Navegador
driver.close()
