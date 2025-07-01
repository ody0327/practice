# p188 도전문제

import datetime
now = datetime.datetime.now()

hi = str(input("입력 : "))
if "안녕" in hi:
    print("안녕하세요.")
elif "몇 시" in hi:
    print(f"지금은 {now.hour}시입니다.")
else:
    print(hi)

