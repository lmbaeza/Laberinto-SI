import sys
import os

def get_path():
    os.system('g++ -std=c++17 -o Labyrinth Labyrinth.cpp')
    os.system('./Labyrinth Labyrinth < map.txt > path.txt')
    path = ''

    with open('path.txt', 'r') as reader:
        path += reader.read()
    
    return path