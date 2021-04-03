import os

def cls():
    '''Clears the console'''
    os.system('cls' if os.name=='nt' else 'clear')