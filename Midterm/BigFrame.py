"""BIG FRAME"""
TEXT1_ = str(input())
TEXT2_ = str(input())
TEXT3_ = str(input())
TEXT4_ = str(input())
TEXT5_ = str(input())
if len(TEXT1_) > len(TEXT2_) and len(TEXT1_) > len(TEXT3_) and\
      len(TEXT1_) > len(TEXT4_) and len(TEXT1_) > len(TEXT5_):
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)
    print(2*"*"+TEXT1_+" "*(len(TEXT1_)-len(TEXT1_))+"*"*2)
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)
    print(2*"*"+len(TEXT1_)*"*"+"*"*2)