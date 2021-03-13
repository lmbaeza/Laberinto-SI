# References
# https://www.youtube.com/watch?v=Xjv1sY630Uc
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from screenshot import screen_component_by_id

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

DIRECTIONS = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

for i in range(100):
    time.sleep(0.5)
    choice = random.choice(DIRECTIONS)
    # press
    print("PRESS")
    ActionChains(driver).key_down(choice).perform()
    time.sleep(0.3)
    # stop pressing
    ActionChains(driver).key_up(choice).perform()

driver.close()