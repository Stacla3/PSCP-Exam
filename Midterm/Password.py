"""Password"""
import math
TEXT_ = str(input())
NUM1_ = False
NUM2_ = False
NUM3_ = False
NUM4_ = False
NUM5_ = 0
LENN_ = len(TEXT_)
for I_ in TEXT_:
    if I_.isalpha():
        NUM1_ = True
    if I_.isupper():
        NUM2_ = True
    if I_.isnumeric():
        NUM3_ = True
    if not I_.isalnum():
        NUM4_ = True
if NUM1_ is True:
    NUM5_ += 26
if NUM2_ is True:
    NUM5_ += 26
if NUM3_ is True:
    NUM5_ += 10
if NUM4_ is True:
    NUM5_ += 32
RESULT_ = math.log(NUM5_**LENN_, 2)
if RESULT_ < 28:
    print(int(RESULT_))
    print("Very Weak")
elif RESULT_ >= 28 and RESULT_ <= 35:
    print(int(RESULT_))
    print("Weak")
elif RESULT_ >= 36 and RESULT_ <= 59:
    print(int(RESULT_))
    print("Reasonable")
elif RESULT_ >= 60 and RESULT_ <= 127:
    print(int(RESULT_))
    print("Strong")
elif RESULT_ >= 128:
    print(int(RESULT_))
    print("Very Strong")
