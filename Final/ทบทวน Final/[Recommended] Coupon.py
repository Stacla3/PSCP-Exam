"""[Recommended] Coupon"""
def main():
    """Start"""
    price = float(input())
    coupon1 = str(input()).split()
    coupon2 = str(input()).split()
    result1 = 0
    result2 = 0
    list1 = []
    if price < float(coupon1[-1]) and price < float(coupon2[-1]):
        print("Nope")
    else:
        if price >= float(coupon1[-1]):
            result1 += price-(float(coupon1[0]))
            list1.append(result1)
        if price >= float(coupon2[-1]):
            result2 += price-(price*(float(coupon2[0])/100))
            list1.append(result2)
        minn = min(float(coupon1[-1]), float(coupon2[-1]))
        if result1 == result2:
            if float(coupon1[-1]) == float(coupon2[-1]):
                print(1, "%.1f" %result1)
            elif minn == float(coupon1[-1]):
                print(1, "%.1f" %result1)
            elif minn == float(coupon2[-1]):
                print(2, "%.1f" %result2)
        elif result1 != result2:
            minn2 = min(list1)
            if minn2 == result1:
                print(1, "%.1f" %result1)
            elif minn2 == result2:
                print(2, "%.1f" %result2)
main()
