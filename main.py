# === Main ===

print("")
print("=== Programs ===")
print("1: Get Power Factor and find PF corrective Capacitor")
print("2: Solve and Simplify Boolean Logic")
print("")
SelectProgram = input("Choose Program:")

if SelectProgram == "1":
    exec(open("PowerFactor.py").read())
elif SelectProgram == "2":
    exec(open("LogicSolver.py").read())
else:
    print("Didn't Work")
