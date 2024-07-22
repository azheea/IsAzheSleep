from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/')
all_status = ["清醒", "睡着"]
status = "清醒"

@app.route("/api", methods=['POST'])
def IsSleep():
    global status  # 声明 status 为全局变量
    key = request.json.get("key")
    _ = request.json.get("status")
    if key != "azhesleep":
        return {"status": "401", "data": "Invalid key"}
    else:
        if request.json.get("status") == status:
            return {"status": "200", "data": "与当前状态相同，因此未更新"}
        else:
            if _ in all_status:
                status = _
                return {"status": "200", "data": "状态已更新"}
            else:
                return {"status": "200", "data": "无效的状态"}

@app.route("/")
def index():
    return render_template("./index.html", status=status)

@app.route("/connect")
def connect():
    return render_template("./connect.html")

if __name__ == '__main__':
    app.run(host="::", port=7788)