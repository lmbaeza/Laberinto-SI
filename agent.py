import time

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

class Agent:

    def __init__(self, driver, level):
        self.driver = driver
        # Ruta que debe tomar el Bot compuesta por caracteres {'L', 'R', 'D', 'U'}
        self.path = ''
        self.level = level
        self.MAP_FILE_NAME = 'img/map-' + str(level) + '.png'
        self.SERIALIZED_MAP_PATH = 'img/serialized-map.png'
        self.MAP_ASCII = 'ascii/map.txt'
        # Lista de Direcciones
        self.DIRECTIONS = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
    
    def percibir(self):
        screen_component_by_id(driver=self.driver, id_name="animation_container", filename=self.MAP_FILE_NAME)
        run_map_processing(level=self.level)
        
    def pensar(self):
        self.path = get_path(level=self.level)
        print("path:", self.path)
    
    def actuar(self):
        # milliseconds = 0.084
        milliseconds = 0.0
        eps_up = 0.0
        eps_down = 0.0
        eps_left = 0.0
        eps_right = 0.0

        if self.level == 1:
            milliseconds = 0.18
            eps_right = 0.04
            eps_left = 0.04
            eps_up = 0.0
            eps_down = 0.0
        elif self.level == 2:
            milliseconds = 0.18
            eps_right = 0.04
            eps_left = 0.04
            eps_up = 0.0
            eps_down = 0.0
        elif self.level == 3:
            milliseconds = 0.18
            eps_right = 0.04
            eps_left = 0.04
            eps_up = -0.04
            eps_down = -0.04

        for direction in self.path:
            time.sleep(0.5)

            if direction == 'U':
                print("Press UP")
                # Selecionar Tecla
                ActionChains(self.driver).key_down(self.DIRECTIONS[0]).perform()
                time.sleep(milliseconds-eps_up)
                # Parar Seleción
                ActionChains(self.driver).key_up(self.DIRECTIONS[0]).perform()
            elif direction == 'D':
                print("Press DOWN")
                # Selecionar Tecla
                ActionChains(self.driver).key_down(self.DIRECTIONS[1]).perform()
                time.sleep(milliseconds-eps_down)
                # Parar Seleción
                ActionChains(self.driver).key_up(self.DIRECTIONS[1]).perform()
            elif direction == 'L':
                print("Press LEFT")
                # Selecionar Tecla
                ActionChains(self.driver).key_down(self.DIRECTIONS[2]).perform()
                time.sleep(milliseconds-eps_left)
                # Parar Seleción
                ActionChains(self.driver).key_up(self.DIRECTIONS[2]).perform()
            elif direction == 'R':
                print("Press RIGHT")
                # Selecionar Tecla
                ActionChains(self.driver).key_down(self.DIRECTIONS[3]).perform()
                time.sleep(milliseconds-eps_right)
                # Parar Seleción
                ActionChains(self.driver).key_up(self.DIRECTIONS[3]).perform()

    def close(self):
        self.driver.close()
    