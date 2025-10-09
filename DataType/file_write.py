# 랜덤 숫자 만들기
import random
# 간단한 한글 리스트 만들기
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 열기
with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤 값으로 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 쓰기
        file.write("{}, {}, {}\n".format(name, weight, height))