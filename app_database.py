import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from modules.storing_guest_name import guest
app = Flask(__name__)
CORS(app)

connection = psycopg2.connect("dbname=final_report user=admin")


@app.route('/')
def index():
    return render_template('welcome_page.html')


@app.route('/who_am_i')
def who_am_i():
    return render_template('juice_world_who_am_i.html')

#
# @app.route('/guest_login')
# def guest_login():
#     return render_template('guest_login.html')
#
#
# @app.route('/storing_guest_name', methods=['POST'])
# def guest_login():
#     guest(connection, request.form)


@app.route('/login_page')
def login_page():
    return render_template('juice_world_login_page.html')


@app.route('/validation', methods=['POST'])
def validation():
    return checking_name_and_password(connection, request.form)


def checking_name_and_password(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select password from employee_detais where password = %(password)s ",
        {'password': validation_data['password']}, )
    returned_rows = cursor.fetchall()
    cursor.close()
    if len(returned_rows) == 0:
        return render_template('welcome_page.html')
    else:
        return beverages()


def beverages():
    menu = database_connection()
    items = []
    for row in menu:
        items.append(row[0])
    return render_template("jinja_items.html", items=items)


def database_connection():
    print("try is running")
    connection = psycopg2.connect(user="admin", host="127.0.0.1", port="5432",
                                  database="final_report")
    cursor = connection.cursor()
    cursor.execute("select name_of_items from items where is_available='yes_hot'")
    record = cursor.fetchall()
    return record






if __name__ == '__main__':
    app.run()