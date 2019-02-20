import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from modules.posting_juice_world_data_to_database import posting_data
from modules.posting_madras_coffee_data_to_database import posting_data

app = Flask(__name__)
CORS(app)
connection = psycopg2.connect("dbname=beverages user=admin")
connection = psycopg2.connect("dbname=madras_coffee user=admin")


def __init__(self, employee_name, password):
    self.employee_name = employee_name
    self.password = password


@app.route('/')
def index():
    return render_template('welcome_page.html')


@app.route('/who_am_i_for_juice_world')
def page2():
    return render_template('juice_world_who_am_i.html')


@app.route('/who_am_i_for_madras_coffee')
def page3():
    return render_template('juice_world_who_am_i.html')


@app.route('/login_page')
def page4():
    return render_template('juice_world_login_page.html')


@app.route('/post-data', methods=['POST'])
def post_user():
    posting_data(connection, request.form)
    return render_template('display.html', shared=request.form)


if __name__ == '__main__':
    app.run()
