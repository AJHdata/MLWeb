from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')




# __main__ 일 경우에만 run 실행
# 위에서부터 실행시키기 때문에 다른 이름이 실행시킬 경우, 서버가 죽기때문
if __name__ == '__main__' :
    app.run(debug=True)