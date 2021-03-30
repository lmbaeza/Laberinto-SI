import sys
import os
import platform

def get_path():
    
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        # Comandos para Linux y Mac
        os.system('g++ -std=c++17 -o Labyrinth Labyrinth.cpp')
        os.system('./Labyrinth < ascii/map.txt > ascii/path.txt')
    elif platform.system() == 'Windows':
        # Comandos para Windows
        os.system('g++ -std=c++17 -o Labyrinth.exe Labyrinth.cpp')
        os.system('Labyrinth.exe < ascii/map.txt > ascii/path.txt')
    
    path = ''

    with open('ascii/path.txt', 'r') as reader:
        path += reader.read()
    
    path = path.replace('DD', 'D')
    path = path.replace('UU', 'U')
    path = path.replace('LL', 'L')
    path = path.replace('RR', 'R')
    return path