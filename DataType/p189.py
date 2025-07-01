integer = int(input("정수를 입력해주세요: "))
'''
if integer % 2 != 0:
    print(f"{integer}는 2로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{integer}는 2로 나누어 떨어지는 숫자입니다.")
if integer % 3 != 0:
    print(f"{integer}는 3으로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{integer}는 3으로 나누어 떨어지는 숫자입니다.")
if integer % 4 != 0:
    print(f"{integer}는 4로 나누어 떨어지는 숫자가 아닙니다.")
else: 
    print(f"{integer}는 4로 나누어 떨어지는 숫자입니다.")
if integer % 5 != 0:
    print(f"{integer}는 5로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{integer}는 5로 나누어 떨어지는 숫자입니다.")
'''

for n in [3, 4, 5, 6, 9, 10]:
    if integer % n != 0:
        print(f"{integer}는 {n}의 배수가 아닙니다.")
    else:
        print(f"{integer}는 {n}의 배수입니다.")