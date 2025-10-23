list_number = [52, 273, 32, 103, 90, 10, 275]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    #ValueError가 발생하는 경우
    print("정수를 입력해라")
    print("exception:", exception)
except IndexError as exception:
    #IndexError가 발생하는 경우
    print("리스트의 인덱스 벗어남")
    print("exception:", exception)