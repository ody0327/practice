limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    sum_value += i
    i += 1
print("1부터 {}까지의 합이 {}을 넘으며 그때의 합은 {}입니다.".format(i-1, limit, sum_value))