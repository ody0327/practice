def test():
    print("함수 호출됨")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())