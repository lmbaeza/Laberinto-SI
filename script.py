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
MAP_ASCII = 'ascii/map.txt'

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
    # Tomar screemshot del mapa
    screen_component_by_id(driver=driver, id_name="animation_container", filename=MAP_FILE_NAME)

    # Procesar la Imagen
    run_map_processing(level=level)

    path = get_path(level=level)

    print('path : ', path)

    # Lista de Direcciones
    DIRECTIONS = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

    # milliseconds = 0.084
    milliseconds = 0.0
    eps_up = 0.0
    eps_down = 0.0
    eps_left = 0.0
    eps_right = 0.0

    if level == 1:
        milliseconds = 0.18
        eps_right = 0.04
        eps_left = 0.04
        eps_up = 0.0
        eps_down = 0.0
    elif level == 2:
        milliseconds = 0.18
        eps_right = 0.04
        eps_left = 0.04
        eps_up = 0.0
        eps_down = 0.0
    elif level == 3:
        milliseconds = 0.18
        eps_right = 0.04
        eps_left = 0.04
        eps_up = 0.0
        eps_down = 0.00

    for direction in path:
        time.sleep(0.5)

        if direction == 'U':
            print("Press UP")
            # Selecionar Tecla
            ActionChains(driver).key_down(DIRECTIONS[0]).perform()
            time.sleep(milliseconds-eps_up)
            # Parar Seleción
            ActionChains(driver).key_up(DIRECTIONS[0]).perform()
        elif direction == 'D':
            print("Press DOWN")
            # Selecionar Tecla
            ActionChains(driver).key_down(DIRECTIONS[1]).perform()
            time.sleep(milliseconds-eps_down)
            # Parar Seleción
            ActionChains(driver).key_up(DIRECTIONS[1]).perform()
        elif direction == 'L':
            print("Press LEFT")
            # Selecionar Tecla
            ActionChains(driver).key_down(DIRECTIONS[2]).perform()
            time.sleep(milliseconds-eps_left)
            # Parar Seleción
            ActionChains(driver).key_up(DIRECTIONS[2]).perform()
        elif direction == 'R':
            print("Press RIGHT")
            # Selecionar Tecla
            ActionChains(driver).key_down(DIRECTIONS[3]).perform()
            time.sleep(milliseconds-eps_right)
            # Parar Seleción
            ActionChains(driver).key_up(DIRECTIONS[3]).perform()

# Cerrar el Navegador
driver.close()
