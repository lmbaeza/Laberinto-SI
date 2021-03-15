from PIL import Image

# ASCII_CHARS = [
#     '1','2','3','4','5','6','7','8','9','0','!',
#     'Q','W','E','R','T','Y','U','I','O','P','A',
#     'S','D','F','G', 'H', 'J', 'K', 'L', 'Ñ', 'Z',
#     'X', 'C', 'V', 'B', 'N', 'M', ',', '[', ']', '/',
#     '*', '-', '+', '$', '%', '&', '(', ')'
# ]

ASCII_CHARS = [
    '1','2','3','4','5','6','7','#','#','#','#',
    '#','W','#','#','T','#','U','#','#','P','#',
    '#','#','#','#', 'H', '#', 'K', '#', '#', '#',
    '.', '#', '#', '#', '#', '#', '#', '#', '#', 'O',
    '*', '#', '#', '#', '#', '#', '(', ')'
]
ASCII_CHARS = ASCII_CHARS[::-1]

DIMENSION = 100

def resize(image, new_width=DIMENSION):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=6):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=DIMENSION):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def map_to_ascii(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in", path)
        return
    image = do(image)

    f = open('map.txt','w')
    f.write(image)
    f.close()
