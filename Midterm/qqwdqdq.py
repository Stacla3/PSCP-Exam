"""ValidVar"""
def main():
    """Start"""
    num1 = int(input())
    for _ in range(num1):
        text = str(input())
    if text == "." or text == "," or text == "!" or text == "?" or text == ":":
        print("Invalid")
    elif text == ";" or text == "“ ”" or text == "'" or text == "-" or text == "()":
        print("Invalid")
    elif text == "if" or text == "else" or text == "if" or text == "while" or text == "for":
        print("Invalid")
    elif text == "True" or text == "False" or text == "continue" or text == "break" or text == "return":
        print("Invalid")
    elif text == "is" or text == "in" or text == "and" or text == "," or text == "from":
        print("Invalid")
    elif text == "as" or text == "pass" or text == "not" or text == "def" or text == "None":
        print("Invalid")
    elif text[0].isnumeric():
        print("Invalid")
    elif text == " ":
        print("Invalid")
    else:
        print("Valid")

main()
