import sys

print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion():", sys.getwindowsversion()) # Windows 전용(codespace에서는 작동하지 않을 수 있음)
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제로 종료합니다.
sys.exit()