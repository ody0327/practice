def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        # 여러가지 처리 수행
        return
        # 파일에 텍스트 입력
        file.write(text)
    except:
        print("오류 발생")
    finally:
        file.close()

write_text_file("test.txt", "안녕하세요!")