from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("gugudan.html")

@app.route("/gugudan")
def gugudan_logic():
    dan_str = request.args.get("dan")
    
    if not dan_str:
        return "단을 입력해주세요."

    try:
        dan = int(dan_str)
        resp = ""
        for x in range(1, 10):
            resp += f"{dan} x {x} = <font color='blue'>{dan * x}</font><br>"
        
        return resp
    except ValueError:
        return "숫자를 정확히 입력해주세요."

if __name__ == "__main__":
    app.run(debug=True)