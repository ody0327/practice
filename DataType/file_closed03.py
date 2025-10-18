try:
    file = open("info.txt", "w")
    예외.발생해라()
except:
    print("오류 발생")
finally:
    file.close()

print("파일이 제대로 닫혔는지 확인")
print("file.closed:", file.closed)