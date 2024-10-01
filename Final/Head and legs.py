"""Rabiy"""
def main():
    """Start"""
    num_a = abs(int(input()))
    num_b = abs(int(input()))
    var_y = (num_b - (4 * num_a)) / (-2)
    var_x = num_a - var_y
    if var_y < 0 or var_x < 0:
        print("Impossible")
    elif num_b % 2 != 0:
        print("Impossible")
    else:
        print(abs(int(var_x)), abs(int(var_y)))
 
main()
