"""FizzBuzz"""
def FizzBuzz():
    """Start"""
    num1_ = int(input())
    for i in range(num1_):
        if (i+1) % 3 == 0 and (i+1) % 15 != 0:
            print("Fizz")
        elif (i+1) % 5 == 0 and (i+1) % 15 != 0:
            print("Buzz")
        elif (i+1) % 15 == 0:
            print("FizzBuzz")
        else:
            print(i+1)

FizzBuzz()
