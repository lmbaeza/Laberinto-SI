import sys
import os

def get_path():
    os.system('g++ -std=c++17 -o Labyrinth Labyrinth.cpp')
    os.system('./Labyrinth Labyrinth < ascii/map.txt > ascii/path.txt')
    path = ''

    with open('ascii/path.txt', 'r') as reader:
        path += reader.read()
    
    path = path.replace('DD', 'D')
    path = path.replace('UU', 'U')
    path = path.replace('LL', 'L')
    path = path.replace('RR', 'R')
    return path