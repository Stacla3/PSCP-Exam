"""Temperatrue"""
def calcu(fever, symbols, want):
    """Start"""
    result1 = 0
    if symbols == "F":
        result1 = (fever-32)*(5/9)
    elif symbols == "K":
        result1 = fever-273.15
    elif symbols == "R":
        result1 = (fever*(5/9))-273.15
    elif symbols == "C":
        result1 = fever
    if want == "F":
        lastone = result1*(9 / 5)+32
    elif want == "K":
        lastone = result1+273.15
    elif want == "R":
        lastone = (result1+273.15)*(9/5)
    else:
        lastone = result1
    return lastone
def answer():
    """ANSWER"""
    fever, symbols, want = float(input()), str(input()), str(input())
    lastone = calcu(fever, symbols, want)
    print("%.2f" %lastone)
answer()
