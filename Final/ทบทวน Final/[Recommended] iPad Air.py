"""[Recommended] iPad Air"""
def main():
    """Start"""
    color = str(input())
    capacity = int(input())
    wifi = str(input())
    list1 = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    list2 = [64, 256]
    list3 = ["Wi-Fi", "Wi-Fi + Cellular"]
    if color in list1 and capacity in list2 and wifi in list3:
        if capacity == list2[0] and wifi == list3[0]:
            print(19900)
        elif capacity == list2[1] and wifi == list3[0]:
            print(24900)
        elif capacity == list2[0] and wifi == list3[1]:
            print(24400)
        elif capacity == list2[1] and wifi == list3[1]:
            print(29400)
    else:
        print("Not Available")
main()
