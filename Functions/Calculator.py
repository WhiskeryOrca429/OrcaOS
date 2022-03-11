def Calc():
    print("Welcome to the calculator")
    mnb = input("Number 1:\n")
    mnc = input("Operator:\n")
    mnd = input("Number 2:\n")

    mnb = float(mnb)
    mnd = float(mnd)

    if mnc == "+":
        print(f"Anwser: {mnb + mnd}")
    if mnc == "-":
        print(f"Anwser: {mnb - mnd}")
    if mnc == "*":
        print(f"Anwser: {mnb * mnd}")
    if mnc == "/":
        print(f"Anwser: {mnb / mnd}")