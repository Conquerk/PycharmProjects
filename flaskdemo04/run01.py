import os

import datetime

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/01-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        #处理上传的文件
        #1.得到上传的文件
        f = request.files['uimg']
        #2.将文件保存在指定的目录处
        #相对路径
        # print('文件名：'+f.filename)
        # f.save('static/'+f.filename)
        #绝对路径
        #当前文件的目录名
        basedir = os.path.dirname(__file__)
        ext = f.filename.split('.')[1]
        # print('完整的上传路径:'+upload_path)
        ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        filename = ftime + '.'+ ext
        upload_path = os.path.join(basedir, 'static/upload',filename)
        f.save(upload_path)
        return 'OK'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')