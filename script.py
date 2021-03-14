import time
import random
import inspect

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from screenshot import screen_component_by_id

from image_to_asciify import map_to_ascii


# Aquí se utilizará Chrome
driver = webdriver.Chrome()
 
# URL de la Pagina
URL = 'https://www.juegosinfantilespum.com/laberintos-online/12-auto-buhos.php'

# Abriendo el sitio web
driver.get(URL)

time.sleep(4)

# Obtener el botón por el id
button = driver.find_element_by_id("animation_container")
 
# Click en el botton
button.click()
print("Click")

time.sleep(1)

screen_component_by_id(driver=driver, id_name="animation_container", filename="map.png")

map_to_ascii("map.png")

# Cargar Mapa es Ascii

mapa = []
with open('map.txt') as grid:
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
