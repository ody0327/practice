min_people = 2
max_people = 10
all_people = 100
memo = {}

def problem(remaining_people, group_size):
    key = str([remaining_people, group_size])
    # 종료 조건
    if key in memo:
        return memo[key]
    if remaining_people < 0:
        return 0
    if remaining_people == 0:
        return 1
    # 재귀 처리
    count = 0
    for i in range(group_size, max_people + 1):
        count += problem(remaining_people - i, i)
    # 메모화 처리
    memo[key] = count
    return count

print(problem(all_people, min_people))
print(memo)