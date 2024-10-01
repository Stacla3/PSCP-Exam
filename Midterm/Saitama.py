"""Saitama"""
import math
NUM1_ = int(input())
NUM2_ = int(input())
NUM3_ = int(input())
NUM4_ = int(input())
NUM5_ = int(input())
NUM6_ = int(input())
NUM7_ = int(input())
NUM8_ = int(input())
RESULT1_ = NUM1_ / NUM5_
RESULT2_ = NUM2_ / NUM6_
RESULT3_ = NUM3_ / NUM8_
RESULT4_ = NUM4_ / NUM7_
if RESULT1_ > RESULT2_ and RESULT1_ > RESULT3_ and RESULT1_ > RESULT4_:
    print(math.ceil(RESULT1_))
elif RESULT2_ > RESULT1_ and RESULT2_ > RESULT3_ and RESULT2_ > RESULT4_:
    print(math.ceil(RESULT2_))
elif RESULT3_ > RESULT2_ and RESULT3_ > RESULT1_ and RESULT3_ > RESULT4_:
    print(math.ceil(RESULT3_))
elif RESULT4_ > RESULT2_ and RESULT4_ > RESULT3_ and RESULT4_ > RESULT1_:
    print(math.ceil(RESULT4_))
elif RESULT1_ == RESULT2_ == RESULT3_ == RESULT4_:
    print(math.ceil(RESULT1_))
