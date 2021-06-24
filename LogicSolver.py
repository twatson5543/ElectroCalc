# === Libraries ===
import math
import os

WinClear = lambda: os.system('cls')
LinClear = lambda: os.system('clear')
WinClear()

# === Functions ===
def LogicToList(UserInput):
    Listed = UserInput.split('+')
    return Listed

def ListToStrings(Listed):
    stringedList2 = (list(str(i)) for i in Listed)
    return stringedList2

# === Steps ===

# User Input for Logic
LogicInput = input("Type your Logic to Solve (A+BC or a+Bc):")

# Seperate parts of logic to OR
LogicList_1 = LogicToList(LogicInput)
print(LogicList_1)

# ds
StringedList = [ListToStrings(LogicList_1)]
print(StringedList)

# === End ===
input("Press Enter to continue...")
exec(open("main.py").read())

# === Libraries ===
import math

# === Functions ===
def LogicToList(UserInput):
    Listed = UserInput.split('+')
    return Listed

def ListToStrings(Listed):
    stringedList2 = Listed.split()
    return stringedList2

# === Steps ===

# User Input for Logic
LogicInput = input("Type your Logic to Solve (A+BC or a+Bc):")

# Seperate parts of logic to OR
LogicList_1 = LogicToList(LogicInput)
print(LogicList_1)

# ds
StringedList = [ListToStrings(LogicList_1)]
print(StringedList)
