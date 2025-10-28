import os
'''
output = os.listdir(".")
print("os.listdir():", output)
print()

print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)
'''
def read_folder(path):
    #폴더의 요소 읽어 들이기
    output = os.listdir(path)
    #폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
        else:
            print("파일:", item)
read_folder(".")