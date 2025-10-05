#내가 쓴 코드
'''
s = input("염기 서열을 입력해주세요: ")

counter = {}

for i in s:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

print(
    f"a의 개수 : {counter['a']}\n"
    f"t의 개수 : {counter['t']}\n"
    f"g의 개수 : {counter['g']}\n"
    f"c의 개수 : {counter['c']}"
)
'''
# 답지 코드
nucleos = input("염기 서열을 입력해주세요: ")
counter = {
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0
}

for nucleo in nucleos:
    counter[nucleo] += 1

for key in counter:
    print(f"{key}의 개수: {counter[key]}")