"""Flatten"""
def main(text):
    """Start"""
    import json
    text1 = json.loads(str(text))
    list1 = []
    for i in text1:
        if isinstance(i, list):
            list1.extend(main(i))
        else:
            list1.append(i)
    return sorted(list1, reverse= True)

print(main(str(input())))
