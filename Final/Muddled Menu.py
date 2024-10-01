"""Muddled Menu"""
def main():
    """Start"""
    list1 = []
    while True:
        text = str(input())
        if "#" in text and text[-1] != "N":
            list1.insert(int(text.split("#")[-1])-1, text[:text.rfind(" ")])  # แทรกMENUลงในlist
        elif "#" in text and text[-1] == "N":
            list1.append(text[:text.rfind(" ")])   #หาตัวที่มี # Nอยู่
        elif text == "SOMETHING'S WRONG":
            list1.clear()
        elif "Can't do: "in text:   # ลบMENUออก
            list1.remove(text[10:])
        elif text == "CLOSED":
            list1.clear()
            break
        elif text == "DONE":
            break
    result = list1.copy()
    result.reverse()
    print("Full Course:", list1, "Reversed:", result)

main()
