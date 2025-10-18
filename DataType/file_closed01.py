try:
    file = open("info.txt", "w")
    file.close()
except:
    print("오류 발생")

print("파일이 제대로 닫혔는지 확인")
print("file.closed:", file.closed)