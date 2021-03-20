import time
import random
import inspect


from screenshot import screen_component_by_id
from image_to_asciify import map_to_ascii
from image_map_processing import run_map_processing

level = 1

MAP_FILE_NAME = 'img/map-' + str(level) + '.png'
SERIALIZED_MAP_PATH = 'img/serialized-map.png'
MAP_ASCII = 'map.txt'

run_map_processing(level=level)
