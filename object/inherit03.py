class CumtomException(Exception):
    def __init__(self):
        super().__init__()
        print("내가 만든 오류!")
    def __str__(self):
        return "오류가 발생했습니다."
    
raise CumtomException