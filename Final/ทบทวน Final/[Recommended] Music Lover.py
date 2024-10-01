"""[Recommended] Music Lover"""
def main():
    """Start"""
    num1 = int(input())
    dict1 = dict()
    list1 = []
    for i in range(num1):
        text = str(input()).split("-")
        if text[0] in dict1:
            dict1[text[0]] += [text[1]]
        else:
            dict1[text[0]] = [text[1]]
    for i in dict1:
        list1.append(i)
        list1.extend(dict1[i])
    for i in list1:
        print(str(i).strip())
main()
