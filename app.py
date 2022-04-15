from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')

# methods 안적으면 GET이 디폴트.
@app.route('/mnist', methods=['GET', 'POST'])
def mnist() :
    if request.method == 'GET' :
        return render_template('mnistform.html')
    else :
        # request.files[' "input태그의 name값" ']
        f = request.files['mnistfile']
        # os.path.dirname(__file__) 는 현재 파일의 경로
        path = os.path.dirname(__file__)+'/upload/' + f.filename
        f.save(path)
        return '성공'

# __main__ 일 경우에만 run 실행
# 위에서부터 실행시키기 때문에 다른 이름이 실행시킬 경우, 서버가 죽기때문
if __name__ == '__main__' :
    app.run(debug=True)