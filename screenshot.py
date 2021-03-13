from PIL import Image

def screen_component_by_id(driver, id_name, filename):
    element = driver.find_element_by_id(id_name)
    location = element.location
    size = element.size
    driver.save_screenshot("image.png")
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open('image.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(filename)
    print("Take Screen")