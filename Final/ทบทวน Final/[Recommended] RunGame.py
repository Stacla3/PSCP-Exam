"""[Recommended] RunGame"""
def main():
    """Start"""
    text = str(input()).split()
    list1 = [0]
    list2 = []
    result = 0
    for i in text:
        list1.append(int(i))
    for i in range(len(list1)-1):
        result = abs(list1[i]-list1[i+1])
        list2.append(result)
    print(sum(list2))
main()
