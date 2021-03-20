# https://stackoverflow.com/questions/7853628/how-do-i-find-an-image-contained-within-an-image/35378944
import cv2
from PIL import Image
import numpy as np

from image_to_asciify import map_to_ascii

LEVEL = 2
FOLDER = "level-"+str(LEVEL)

method = cv2.TM_SQDIFF_NORMED

SERIALIZED_MAP = 'img/serialized-map.png'

def identify_object(small_image, map_image, color):
    result = cv2.matchTemplate(small_image, map_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on map_image
    cv2.rectangle(map_image, (MPx, MPy),(MPx+tcols,MPy+trows), color, -1)

def run_levels(level, map_image):
    # Read the images from the file
    home_image = cv2.imread('img/home.png')
    car_image = cv2.imread('img/car.png')

    # RGB Colors
    blue = (0, 255, 0)
    red = (0, 0, 255)
    green = (255, 0, 0)

    if level == 1:
        buho1_image = cv2.imread(FOLDER + '/buho-1.png')
        buho2_image = cv2.imread(FOLDER + '/buho-2.png')
        buho3_image = cv2.imread(FOLDER + '/buho-3.png')
        identify_object(home_image, map_image, red)
        identify_object(car_image, map_image, blue)
        identify_object(buho1_image, map_image, green)
        identify_object(buho2_image, map_image, green)
        identify_object(buho3_image, map_image, green)
    elif level == 2:
        buho1_image = cv2.imread(FOLDER + '/buho-1.png')
        buho2_image = cv2.imread(FOLDER + '/buho-2.png')
        buho3_image = cv2.imread(FOLDER + '/buho-3.png')
        buho4_image = cv2.imread(FOLDER + '/buho-4.png')
        buho5_image = cv2.imread(FOLDER + '/buho-5.png')
        identify_object(home_image, map_image, red)
        identify_object(car_image, map_image, blue)
        identify_object(buho1_image, map_image, green)
        identify_object(buho2_image, map_image, green)
        identify_object(buho3_image, map_image, green)
        identify_object(buho4_image, map_image, green)
        identify_object(buho5_image, map_image, green)
    elif level == 3:
        buho1_image = cv2.imread(FOLDER + '/buho-1.png')
        buho2_image = cv2.imread(FOLDER + '/buho-2.png')
        buho3_image = cv2.imread(FOLDER + '/buho-3.png')
        buho4_image = cv2.imread(FOLDER + '/buho-4.png')
        buho5_image = cv2.imread(FOLDER + '/buho-5.png')
        buho6_image = cv2.imread(FOLDER + '/buho-6.png')
        identify_object(home_image, map_image, red)
        identify_object(car_image, map_image, blue)
        identify_object(buho1_image, map_image, green)
        identify_object(buho2_image, map_image, green)
        identify_object(buho3_image, map_image, green)
        identify_object(buho4_image, map_image, green)
        identify_object(buho5_image, map_image, green)
        identify_object(buho6_image, map_image, green)

def serialized(path):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    white = (256, 256, 256)
    black = (0, 0, 0)

    eps = 10

    img = Image.open(path)
    pixels = img.load() # creates the pixel map
    for i in range(img.size[0]):    
        for j in range(img.size[1]):
            if (102-eps, 102-eps, 102-eps) <= pixels[i,j] and pixels[i,j] <= (102+eps, 102+eps, 102+eps):
                pixels[i, j] = white
            elif pixels[i, j]==blue or pixels[i,j]!=red and pixels[i,j]!=green:
                pixels[i, j] = black
            
    img.save(path)
    

map_image = cv2.imread('img/map-' + str(LEVEL) + '.png')

run_levels(LEVEL, map_image)

# Display the original image with the rectangle around the match.
# cv2.imshow('output', map_image)

cv2.imwrite(SERIALIZED_MAP, map_image)
# The image is only displayed if we call this

serialized(SERIALIZED_MAP)

map_to_ascii(SERIALIZED_MAP)
# cv2.waitKey(0)