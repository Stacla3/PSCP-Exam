"""Day2011"""
def main():
    """Start"""
    date = int(input())
    month = int(input())
    calender = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday"\
                , 4 : "Thursday", 5 : "Friday", 6 : "Saturday"\
                    , 7 : "Sunday"}
    day1ofmonth = {1 : 6, 2 : 2, 3 : 2, 4 : 5, 5 : 7, 6 : 3\
        , 7 : 5, 8 : 1, 9 : 4, 10 : 6, 11 : 1, 12 : 4}
    result = 0
    if month in day1ofmonth.keys():
        result = day1ofmonth[month]
    for _ in range(1, date):
        result += 1
        if  result % 8 == 0:
            result = 0
            result += 1
    print(calender[result])

main()
