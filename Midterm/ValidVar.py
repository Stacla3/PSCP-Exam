"""ValidVar"""
def main():
    """Start"""
    num1 = int(input())
    for _ in range(num1):
        text = str(input()).strip(" ")
        if "!" in text or "\"" in text or "#" in text or "$" in text or "%" in text\
        or "`" in text or "{" in text or "|" in text or "}" in text or "~" in text:
            print("Invalid")
        elif "&" in text or "'" in text or "(" in text or "*" in text or "+" in text\
            or "," in text or "-" in text or "." in text or "/" in text or ":" in text:
            print("Invalid")
        elif ";" in text or "<" in text or "=" in text or ">" in text or "?" in text\
            or "@" in text or "[" in text or "\\" in text or "]" in text or "^" in text:
            print("Invalid")
        elif text == "if" or text == "else" or text == "elif" or text == "while" or text == "for":
            print("Invalid")
        elif text == "True" or text == "False" or text == "continue" or text == "break" \
            or text == "return":
            print("Invalid")
        elif text == "is" or text == "in" or text == "and" or text == "or" or text == "from":
            print("Invalid")
        elif text == "as" or text == "pass" or text == "not" or text == "def" or text == "None":
            print("Invalid")
        elif text[0].isnumeric() == True:
            print("Invalid")
        elif " " in text or ")" in text:
            print("Invalid")
        elif text.lstrip(" ") == True or text.rstrip(" ") == True or text.strip(" ") == True:
            print("Valid")
        else:
            print("Valid")

main()
