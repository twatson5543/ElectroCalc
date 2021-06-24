import time
import os

clear = lambda: os.system('cls')
clear()
# === Main ===

print("")
print("=== Programs ===")
print("0: End Program")
print("1: Get Power Factor and find PF corrective Capacitor")
print("2: Solve and Simplify Boolean Logic")
print("")
SelectProgram = input("Choose Program:")

if SelectProgram == "1":
    exec(open("PowerFactor.py").read())
elif SelectProgram == "0":
    print("Goodbye")
    time.sleep(1)
elif SelectProgram == "2":
    exec(open("LogicSolver.py").read())
else:
    print("Incorrect Value")
    time.sleep(1)
    exec(open("main.py").read())
