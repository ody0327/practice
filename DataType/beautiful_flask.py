from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    target = request.urlopen("https://www.kma.go.kr/plus/rss/mid-term-rss3.jsp?stnId=108")

    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("lcation"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string)