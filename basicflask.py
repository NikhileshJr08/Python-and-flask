from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the home page!</h1>'


@app.route('/puppy_latin/<name>')
def puppu(name):
    temp = ''
    if name[-1] == "y":
        temp = name[:-1] + "iful"
    else:
        temp = name + "y"

    return "Your latin puppy name is {}".format(temp.upper())

if __name__ == "__main__":
    app.run(debug=True)
