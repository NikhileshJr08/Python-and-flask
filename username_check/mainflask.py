from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_check')
def report_check():

    lower_letter = False
    upper_letter = False
    end_num = False
    username = request.args.get("username")

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    end_num = username[-1].isdigit()

    report = lower_letter and upper_letter and end_num

    return render_template('report.html',report = report, lower_letter = lower_letter,upper_letter = upper_letter, end_num = end_num)

if __name__ == '__main__':
    app.run(debug=True)
