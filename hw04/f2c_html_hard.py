from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
<html>
<head><meta charset="UTF-8"><title>단위 변환기</title></head>
<body>
    <form method="GET" action="/calc">
        <h2>🌡️ 온도 변환 (화씨 -> 섭씨)</h2>
        <label>화씨(F) : <input type="text" name="f_temp"></label>
        <button type="submit">변환하기</button>
        
        <br><br>
        <hr>
        
        <h2>📏 길이 변환 (cm -> inch)</h2>
        <label>길이(cm) : <input type="text" name="cm"></label>
        <button type="submit">변환하기</button>
    </form>
</body>
</html>
"""

@app.route("/calc")
def converter():
    f_val = request.args.get("f_temp")
    cm_val = request.args.get("cm")
    
    resp = "<html>"
    resp += "<head><meta charset='UTF-8'></head>"
    resp += "<body>"


    if f_val:
        f_temp = float(f_val)
        c_temp = (f_temp - 32) * 5 / 9
        
        resp += f"<font color='blue'>{f_temp}F는 {c_temp:.2f}C입니다.</font><br>"

    
    if cm_val:
        cm = float(cm_val)
        inch = cm / 2.54
        
        resp += f"<font color='blue'>{cm}cm는 {inch:.2f}inch입니다.</font><br>"

    resp += "<br><a href='/'>뒤로 가기</a>"
    resp += "</body></html>"
    
    print(resp) 
    return resp

if __name__ == "__main__":
    app.run(debug=True)