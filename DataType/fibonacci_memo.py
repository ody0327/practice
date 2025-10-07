dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    
for i in range(10, 51, 10):
    print(f"fibonacci({i}) = {fibonacci(i)}")