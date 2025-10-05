a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        for j in i:
            output.append(j)
    else:
        output.append(i)

print(output)