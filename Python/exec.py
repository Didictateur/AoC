from _2024._2.main import *
from src.parse_data import *

import os
import sys
import time

def test1(y: int, d: int, integer: bool=False):
    # os.system("clear")
    print("test1:")
    L = parse(y, d, integer, True)
    print(result1(L))

def challenge1(y: int, d: int, integer: bool=False):
    # os.system("clear")
    print("challenge1:")
    t = time.time()
    L = parse(y, d, integer)
    print(result1(L))
    dt = time.time()-t
    print(f"done in {dt}s")

def test2(y: int, d: int, integer: bool=False):
    # os.system("clear")
    print("test2:")
    L = parse(y, d, integer, True)
    print(result2(L))

def challenge2(y: int, d: int, integer: bool=False):
    # os.system("clear")
    print("challenge2:")
    t = time.time()
    L = parse(y, d, integer)
    print(result2(L))
    dt = time.time() - t
    print(f"done in {dt}s")

def print_results(y: int, d: int, integer: bool=False, test: bool=True, challenge: bool=True):

    os.system("clear")
    print(f"{y} day {d}\n")

    if test:
        test1(y, d, integer)
        print()
    
    if challenge:
        challenge1(y, d, integer)
        print()
    
    if test:
        test2(y, d, integer)
        print()
    
    if challenge:
        challenge2(y, d, integer)
        print()

print_results(2024, 2, True, True, True)
