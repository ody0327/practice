import datetime

now = datetime.datetime.now()

if 3 <= now.month <- 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 6 <= now.month < 9:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

if 9 <= now.month < 12:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

if now.month == 12 or now.month < 3:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

