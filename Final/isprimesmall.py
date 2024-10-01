"""isprime_small"""
def isprinme(num1):
    """Start"""
    if num1 < 2:
        return False
    if num1 == 3 or num1 == 5:
        return True
    for i in range(4, int(num1**0.5)+1):
        if num1 % i == 0:
            return False
    return True
if isprinme(int(input())):
    print(True)
else:
    print(False)
