"""Coupon"""
def main():
    """Start"""
    price = float(input())
    promo1, promo2 = str(input()).split(), str(input()).split()
    set1, list1 = set(), []
    result1, result2 = 0, 0
    if price < float(promo1[-1]) and price < float(promo2[-1]):
        print("Nope")
    else:
        if price >= float(promo1[-1]):
            result1 += price - float(promo1[0])
            set1.add(float(promo1[-1]))
            list1.append(result1)
        if price >= float(promo2[-1]):
            result2 += price*((100-(float(promo2[0])))/100)
            set1.add(float(promo2[-1]))
            list1.append(result2)
        if result1 == result2:
            if len(set1) == 1:
                print(1, "%.1f" %result1)
            elif min(set1) == float(promo1[-1]) and len(set1) > 1:
                print(1, "%.1f" %result1)
            elif min(set1) == float(promo2[-1]) and len(set1) > 1:
                print(2, "%.1f" %result2)
        elif result1 != result2:
            if min(list1) == result1:
                print(1, "%.1f" %(min(list1)))
            elif min(list1) == result2:
                print(2, "%.1f" %(min(list1)))
main()
