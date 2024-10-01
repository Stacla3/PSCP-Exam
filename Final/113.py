"""113"""
def main(text):
    """Start"""
    if "113" in text:
        text = text.replace("113", "")
        return main(text)
    else:
        return text
print(main(str(input())))
Helloooo