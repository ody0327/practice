count = 0
def TowerOfHanoi(plates, pillar_start, pillar_target, pillar_sub):
    global count
    if plates == 1:
        print(pillar_start, "->", pillar_target)
        count += 1
    else:
        TowerOfHanoi(plates - 1, pillar_start, pillar_sub, pillar_target)
        print(pillar_start, "->", pillar_target)
        count += 1
        TowerOfHanoi(plates - 1, pillar_sub, pillar_target, pillar_start)

n = int(input("원판의 개수를 입력해주세요: "))
TowerOfHanoi(n, "A탑", "B탑", "C탑")
print(f"이동 횟수는 {count}회입니다.")