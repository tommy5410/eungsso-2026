from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Flask 구구단 홈</title>
    </head>
    <body>
        <form method="GET" action="/gugu">
            <h2>구구단 출력하기</h2>
            <label>단 입력 : 
                <input type="text" name="dan" placeholder="예: 5">
            </label>
            <button type="submit">출력하기</button>
        </form>
    </body>
    </html>
    """

@app.route("/gugu")
def gugudan():
    dan_str = request.args.get("dan", "5")
    
    try:
        dan = int(dan_str)
    except ValueError:
        return "<h3>숫자를 입력해주세요!</h3><a href='/'>뒤로 가기</a>"

  
    resp = "<html>"
    resp += "<head><meta charset='UTF-8'><title>Gugudan Result</title></head>"
    resp += "<body>"
    resp += f"<h1>{dan}단 결과 페이지</h1>"
    
    for x in range(1, 10):
        
        resp += f"<font color='blue'>{dan} x {x} = {dan * x}</font>"
        resp += "<br>"

    resp += "<br><a href='/'>다시 입력하기</a>"
    resp += "</body>"
    resp += "</html>"

    return resp

if __name__ == "__main__":
    app.run(debug=True)