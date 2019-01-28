from flask import Flask, render_template

app = Flask(__name__)

@app.route("/00-homework")
def homework():
    dic = {
        'title':'橄榄树',
        'author':'羽凡',
        'music':'乃亮',
        'singer':'宝强',

    }
    return render_template("00-homework.html",params=dic)

if __name__ == "__main__":
    app.run(debug=True)