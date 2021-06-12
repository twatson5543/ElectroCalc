import math

# ==== Values ====
Voltage = int(input("Type Voltage:         "))
hz = int(input("Type Hz:              "))
resistance = int(input("Type Resistor Value:  "))
inductance = float(input("Type Inductor Value:  "))

#
#
#
#
#
# ==== Functions ====
def Xl(l):
    XofL = 2 * math.pi * hz * l
    return XofL

def ZtotalMag_1(Xl):
    real_1 = ((Xl) * (Xl)) + ((resistance) * (resistance))
    real_final = math.sqrt(real_1)
    return real_final

def ZtotalAng_1(Xl):
    imag_1 = Xl / resistance
    imag_2 = math.atan(imag_1)
    imag_final = math.degrees(imag_2)
    return imag_final

def GetCurrent(zTotal):
    Current = Voltage / zTotal
    return Current

def GetCurrentAngle(Zdeg):
    CurrentDeg = -Zdeg
    return CurrentDeg

def GetTruePower(It):
    TruePower = ((It) * (It)) * resistance
    return TruePower

def GetTruePower2(S,zAng):
    TruePower = (S) * (math.cos(math.radians(zAng)))
    return TruePower

def GetApparentPower(Zt,It):
    ApparentPower = ((It)*(It)*Zt)
    return ApparentPower

def GetReactPower(S,zAng):
    ReactivePower = (S) * (math.sin(math.radians(zAng)))
    return ReactivePower

def Xsolve(Q):
    X = (Voltage * Voltage) / Q
    return X

def Csolve(Xc):
    C = 1 / (2 * math.pi * hz * Xc)
    return C

def XofCsolve(Cval):
    XoC = 1 / (2 * math.pi * hz * Cval)
    return XoC

def GetRealNum(realVal,realAng):
    realMag = float((math.cos(math.radians(realAng))))
    realMag2 = round(realMag,12)
    realMag3 = realMag2 * realVal
    return realMag3

def GetImagNum(realVal,realAng):
    ImagNum1 = float((math.sin(math.radians(realAng))))
    ImagNum2 = round(ImagNum1,12)
    ImagNum3 = ImagNum2 * realVal
    return ImagNum3

def GetMag(realVal,ImagVal):
    real_1 = ((ImagVal) * (ImagVal)) + ((realVal) * (realVal))
    real_final = math.sqrt(real_1)
    return real_final

def GetAng(realVal, ImagVal):
    imag_1 = ImagVal / realVal
    imag_2 = math.atan(imag_1)
    imag_final = math.degrees(imag_2)
    return imag_final
#
#
#
#
#
# ==== Math Steps ====

# >> Get Xl
XofL = Xl(inductance)

# >> Get Total Z
zTotalReal_1 = ZtotalMag_1(XofL)
zTotalDeg_1 = ZtotalAng_1(XofL)

# >> Get Current
UnCorI = GetCurrent(zTotalReal_1)
UnCorIang = GetCurrentAngle(zTotalDeg_1)

# >> Real Power
UnCorTruePower = GetTruePower(UnCorI)

# >> Apparent Power
UnCorAppPower = GetApparentPower(Zt=zTotalReal_1, It=UnCorI)

# >> Reactive Power
UnCorReactPower = GetReactPower(S=UnCorAppPower, zAng=zTotalDeg_1)

# >> Solve for X
XofC = Xsolve(UnCorReactPower)

# >> Solve for C
Cvalue = Csolve(XofC)
tCvalue = 0.000022 # <-------- Temporary Value

# >> Find Z Total
ZrCorrect = resistance
ZrAng = float(0)
ZlCorrect = XofL
ZlAng = float(90)
ZcCorrect = XofCsolve(Cvalue)
ZcAng = float(-90)


NumRealSum = GetRealNum(realVal=ZrCorrect, realAng=ZrAng) + GetRealNum(realVal=ZlCorrect, realAng=ZlAng) + GetRealNum(realVal=ZcCorrect, realAng=ZcAng)
NumImagSum = GetImagNum(realVal=ZrCorrect, realAng=ZrAng) + GetImagNum(realVal=ZlCorrect, realAng=ZlAng) + GetImagNum(realVal=ZcCorrect, realAng=ZcAng)

#print(NumRealSum)
#print(NumImagSum)

DenRealSum1 = GetRealNum(realVal=ZrCorrect, realAng=ZrAng) + GetRealNum(realVal=ZlCorrect, realAng=ZlAng)
DenImagSum1 = GetImagNum(realVal=ZrCorrect, realAng=ZrAng) + GetImagNum(realVal=ZlCorrect, realAng=ZlAng)

#print(DenRealSum1)
#print(DenImagSum1)

DenMag1 = GetMag(realVal=DenRealSum1, ImagVal=DenImagSum1)
DenAng1 = GetAng(realVal=DenRealSum1, ImagVal=DenImagSum1)

#print("Den:",DenMag1)
#print("Den:",DenAng1)

NumMag1 = GetMag(realVal=NumRealSum, ImagVal=NumImagSum)
NumAng1 = GetAng(realVal=NumRealSum, ImagVal=NumImagSum)

#print("Num:",NumMag1)
#print("Num:",NumAng1)

DenMultiMag = DenMag1 * ZcCorrect
DenMultiAng = DenAng1 + ZcAng

#print("Den:",DenMultiMag)
#print("Den:",DenMultiAng)


ZtotalMag1 = NumMag1 / DenMultiMag
ZtotalAng1 = NumAng1 - DenMultiAng

#print(ZtotalMag1)
#print(ZtotalAng1)

ZtotalMagCorrect = 1 / ZtotalMag1
ZtotalAngCorrect = -1 * ZtotalAng1

#print("Ztotal Mag:",ZtotalMagCorrect)
#print("Ztotal Ang:",ZtotalAngCorrect)

# >>> Find New Total Current

CorrectI = Voltage / ZtotalMagCorrect
CorrectIang = ZtotalAngCorrect * -1

# >>> Find New Apparent Power

CorrectAppPower = GetApparentPower(Zt=ZtotalMagCorrect, It=CorrectI)

# >>> Find New True Power

CorrectTruePower = GetTruePower2(CorrectAppPower,ZtotalAngCorrect)

# >>> Find New Reactive Power

CorrectReactPower = GetReactPower(CorrectAppPower,ZtotalAngCorrect)

# >>> Find Power Factor

PowerFactor = CorrectTruePower / CorrectAppPower

#
#
#
#
#
# ==== Proof ====


# -- Uncorrected Values --
print("")
print("Uncorrected Values:")
print("Xl = ",str(XofL) + "Ω∡-90∘")
print("Z Total =", str(zTotalReal_1) + "Ω∡" + str(zTotalDeg_1) + "∘")
print("I Total =",str(UnCorI) + "Ω∡" + str(UnCorIang) + "∘")
print("True Power (P):", UnCorTruePower)
print("Apparent Power (S):", UnCorAppPower)
print("Reactive Power (Q):",UnCorReactPower)

print("")
print("Corrective Capacitance:")
print("Xc =", str(XofC) + "∡-90∘")
print("C =", str(Cvalue)+"F")
print("Capacitor Value =", str((Cvalue * math.pow(10, 6))) + "μF")

print("")
print("Corrected Values:")
print("Z Total =", str(ZtotalMagCorrect) + "∡" + str(ZtotalAngCorrect) + "∘")
print("I Total =", str(CorrectI) + "∡" + str(CorrectIang) + "∘")
print("True Power (P):", CorrectTruePower)
print("Apparent Power (S):", CorrectAppPower)
print("Reactive Power (Q):", CorrectReactPower)

print("")
print("Power Factor:",PowerFactor)

"""
val1 = (GetRealNum(realVal=ZrCorrect,realAng=ZrAng))
val2 = GetRealNum(realVal=ZlCorrect, realAng=ZlAng)
val3 = GetRealNum(realVal=ZcCorrect, realAng=ZcAng)
print(val1)
print(val2)
print(val3)
"""
