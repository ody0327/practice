def TowerOfHanoi(plates, pillar_start, pillar_target, pillar_sub):
    if plates == 1:
        print(pillar_start, "->", pillar_target)
    else:
        TowerOfHanoi(plates - 1, pillar_start, pillar_sub, pillar_target)
        print(pillar_start, "->", pillar_target)
        TowerOfHanoi(plates - 1, pillar_sub, pillar_target, pillar_start)

n = int(input("원판의 개수를 입력해주세요: "))
TowerOfHanoi(n, "A탑", "B탑", "C탑")