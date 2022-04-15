from flask import Flask, render_template, request
import os, pickle
from PIL import Image
import numpy as np



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

        # 이미지 수치화, convert 그레이로 스케일링
        img = Image.open(path).convert('L')
        # 흰색 검은색 반전시키기
        img = np.resize(img,(1,784))
        # img = 255 - img


        # 이미지 열기
        mpath = os.path.dirname(__file__) + '/model1.pickle'
        with open(mpath, 'rb') as f :
            model = pickle.load(f)
        
        pred = model.predict(img)

        # return '성공!!' + str(pred) # 결과 확인용 return
        return render_template('mnistresult.html', data=pred)

# __main__ 일 경우에만 run 실행
# 위에서부터 실행시키기 때문에 다른 이름이 실행시킬 경우, 서버가 죽기때문
if __name__ == '__main__' :
    app.run(debug=True)