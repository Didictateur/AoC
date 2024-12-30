import os
import sys

if __name__=="__main__":
    if len(sys.argv) < 3:
        raise Exception("Need a year and a day in argument in order to work")
    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    except:
        raise Exception(f"This is not a valide arguments: {sys.argv[1]} {sys.argv[2]}")
    
    integer = False
    if len(sys.argv) > 3:
        if sys.argv[3] in {"True", "1", "true", "t", "T"}:
            integer = True
    
    test = False
    challenge = False
    if "-t" in sys.argv:
        test = True
    elif "-c" in sys.argv:
        challenge = True
    else:
        test = True
        challenge = True

    path = os.getcwd()
    path_to_python = sys.executable

    with open(f"{path}/exec.py", 'w') as f:
        f.write(f"from _{year}._{day}.main import *\n")
        
        with open(f"{path}/code.txt", "r") as code:
            f.write(code.read())
        
        f.write(f"\n\nprint_results({year}, {day}, {integer}, {test}, {challenge})\n")
    
    os.system(f"{path_to_python} {path}/exec.py")