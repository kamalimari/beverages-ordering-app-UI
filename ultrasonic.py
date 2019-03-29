from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def employee_login_page_juice_world():
    rows = method()
    values_ = []
    for row in rows:
        values_.append(row)
    bin1_ = values_[0]
    bin2_ = values_[1]
    return render_template('ultrasonic.html', bin1=bin1_, bin2=bin2_)


def method():
    d1 = 1
    d2 = 2
    return d1, d2


if __name__ == '__main__':
    app.run()
