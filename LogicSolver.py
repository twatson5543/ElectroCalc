# === Libraries ===
import math

# === Functions ===
def LogictoList(UserInput):
    Listed = UserInput.split('+')
    return Listed

def ListToStrings(Listed):
    stringedList = (str(i) for i in Listed)
    return stringedList

# === Steps ===

# User Input for Logic
LogicInput = input("Type your Logic to Solve (A+BC or a+Bc):")

# Seperate parts of logic to OR
LogicList_1 = LogictoList(LogicInput)
print(LogicList_1)

StringedList = ListToStrings(LogicList_1)
print(StringedList)
