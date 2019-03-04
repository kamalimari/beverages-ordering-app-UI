import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection = psycopg2.connect("dbname=beverages user=admin")


@app.route('/')
def index():
    return render_template('welcome_page.html')


@app.route('/who_am_i')
def who_am_i():
    return render_template('who_am_i.html')


@app.route('/employee_login_page')
def login_page():
    return render_template('employee_login_page.html')


# @app.route('/guest_login')
# def guest_login():
#     return render_template('guest_login.html')


@app.route('/vendor_page')
def vendor_page():
    return render_template('vendor_personal_page.html')


@app.route('/vendor_login_page')
def vendor_login_page():
    return render_template('vendor_login_page.html')


@app.route('/employee_validation', methods=['POST'])
def employee_validation():
    return checking_name_and_password(connection, request.form)


def checking_name_and_password(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select password from employee_details where password = %(password)s ",
        {'password': validation_data['password']})
    returned_rows = cursor.fetchall()
    cursor.close()
    if len(returned_rows) == 0:
        return render_template('welcome_page.html')
    else:
        return render_template('ordering_page.html')


@app.route('/vendor_validation', methods=['POST'])
def vendor_validation():
    return checking_name_and_password_for_vendor(connection, request.form)


def checking_name_and_password_for_vendor(connection, validation_data):
    cursor = connection.cursor()
    if cursor.execute(
        "select vendor_password from vendor_details where vendor_password = %(password)s and shop_no = '1'",
        {'password': validation_data['password']}):
        returned_cold = cursor.fetchall()
        cursor.close()
        if len(returned_cold) == 0:
            return render_template('welcome_page.html')
        else:
            return beverages_cold()

    if cursor.execute("select vendor_password from vendor_details where vendor_password = %(password)s and shop_no = '1'",
        {'password': validation_data['password']}):
        returned_hot = cursor.fetchall()
        cursor.close()
        if len(returned_hot) == 0:
            return render_template('welcome_page.html')
        else:
            return beverages_hot()

def beverages_cold():
    menu = database_connection()
    items = []
    for row in menu:
        items.append(row[0])
    return render_template("jinja_items.html", items=items)


def database_connection():
    print("try is running")
    cursor = connection.cursor()
    cursor.execute("select name_of_items from items where is_available='yes' and type='cold'")
    record = cursor.fetchall()
    cursor.close()
    return record


def beverages_hot():
    menu = database_connection()
    items = []
    for row in menu:
        items.append(row[0])
    return render_template("jinja_items.html", items=items)


def database_connection():
    print("try is running")
    cursor = connection.cursor()
    cursor.execute("select name_of_items from items where is_available='yes' and type='hot'")
    record = cursor.fetchall()
    cursor.close()
    return record


@app.route('/juice_report')
def report():
    return render_template('report_calculation.html')


@app.route('/calculation')
def calculation_():
    cost = calculation_juice()
    return render_template("display.html", items=cost)


def calculation_juice():
    cursor = connection.cursor()
    cursor.execute(
        "select sum(cost*count)from items inner join order_page on items.serial_id = order_page.serial_id where type = 'cold';")
    matches = cursor.fetchall()
    cursor.close()
    return matches


if __name__ == '__main__':
    app.run(debug=True)
