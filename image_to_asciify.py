from PIL import Image

# [@] Representa la localización del carro
# [X] Representa la localización de la casa
# [#] Representa la localizacion del muro
# [.] Representa la localización de la carretera

ASCII_CHARS = [
    '#','#','#','#','#','#','#','.','#','#','#',
    '#','#','#','#','#','#','#','#','#','#','#',
    '#','#','#','@', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', 'X', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#'
]

# ASCII_CHARS = [
#     '1','2','3','4','5','6','7','.','9','0', 'Q',
#     'W','E','R','T','Y','Y','U','I','O','P','A',
#     'S','D','F','G', 'H', 'I', 'J', 'K', 'L', 'Ñ',
#     'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '+', '-',
#     '#', '@', '$', '%', '&', '/', '(', '*'
# ]

ASCII_CHARS = ASCII_CHARS[::-1]

DIMENSION = 45

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

def find_coordenate(target_char, grid, n, m):
    maximum_width = 0
    maximum_height = 0
    first_x = None
    first_y = None
    for i in range(n):
        count_width = 0
        count_height = 0
        for j in range(m):
            if grid[i][j] == target_char:
                count_width += 1
                count_height = 1
                if first_x is None:
                    first_x = i
                    first_y = j
            else:
                count_width = 0
            maximum_width = max(maximum_width, count_width)
        maximum_height += count_height
    
    start_x = first_x + (maximum_height // 2) # - int(maximum_height%2!=0)
    start_y = first_y + (maximum_width // 2) # - int(maximum_width%2!=0) + 1
    return start_x, start_y

def add_start_end(grid):
    grid = grid.split('\n')
    n = len(grid)
    m = len(grid[0])

    
    startA_x, startA_y = find_coordenate('@', grid, n, m)
    startB_x, startB_y = find_coordenate('X', grid, n, m)

    for i in range(n):
        for j in range(m):
            if i==startA_x and j==startA_y:
                row = []
                row[:0] = grid[i]
                row[j] = 'A'
                grid[i] = ''.join(row)
            elif i==startB_x and j==startB_y:
                row = []
                row[:0] = grid[i]
                row[j] = 'B'
                grid[i] = ''.join(row)
                
    
    grid = '\n'.join(grid)
    grid = str(n) + ' ' + str(m) + '\n' + grid
    return grid

def map_to_ascii(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in", path)
        return
    image = do(image)

    image = add_start_end(image)

    print(image)
    f = open('ascii/map.txt','w')
    f.write(image)
    f.close()
