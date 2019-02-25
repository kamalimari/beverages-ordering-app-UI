import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from modules.posting_juice_world_data_to_database import juice_world_data
from modules.posting_madras_coffee_data_to_database import madras_coffee_data

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


@app.route('/juice_world_who_am_i')
def who_am_i_juice_world():
    return render_template('juice_world_who_am_i.html')


@app.route('/madras_coffee_who_am_i')
def who_am_i_madras_coffee():
    return render_template('madras_coffee_who_am_i.html')


@app.route('/login_page_for_juice_world')
def login_page_juice_world():
    return render_template('juice_world_login_page.html')


@app.route('/login_page_for_madras_coffee')
def login_page_madras_coffee():
    return render_template('madras_coffee_login_page.html')


@app.route('/post_data_juice_world', methods=['POST'])
def post_data_juice_world():
    juice_world_data(connection, request.form)
    return render_template('display.html', shared=request.form)


@app.route('/post_data_madras_coffee', methods=['POST'])
def post_data_madras_coffee():
    madras_coffee_data(connection, request.form)
    return render_template('display.html', shared=request.form)


if __name__ == '__main__':
    app.run()