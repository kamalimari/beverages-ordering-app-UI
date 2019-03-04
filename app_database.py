import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection = psycopg2.connect("dbname=beverages user=admin")


@app.route('/')
def index():
    return render_template('welcome_page.html')


@app.route('/who_am_i_juice_world')
def who_am_i_juice_world():
    return render_template('who_am_i_juice_world.html')


@app.route('/employee_login_page_juice_world')
def employee_login_page_juice_world():
    return render_template('employee_login_page_juice_world.html')


# @app.route('/guest_login')
# def guest_login():
#     return render_template('guest_login.html')


@app.route('/vendor_page_juice_world')
def vendor_page_juice_world():
    return render_template('vendor_personal_page_juice_world.html')


@app.route('/vendor_login_page_juice_world')
def vendor_login_page_juice_world():
    return render_template('vendor_login_page_juice_world.html')


@app.route('/employee_validation_juice_world', methods=['POST'])
def employee_validation_juice_world():
    return checking_name_and_password(connection, request.form)


def checking_name_and_password(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select password from employee_details where password = %(password)s ",
        {'password': validation_data['password']})
    returned_rows = cursor.fetchall()
    rows_ = returned_rows[0]
    insert_the_password_id = "insert into order_page (name_id) (select name_id from employee_details where password = %s)"
    cursor.execute(insert_the_password_id, (rows_[0],))
    connection.commit()
    cursor.close()
    if len(returned_rows) == 0:
        return render_template('welcome_page.html')
    else:
        return render_template('ordering_page.html')


@app.route('/vendor_validation_juice_world', methods=['POST'])
def vendor_validation_juice_world():
    return checking_name_and_password_for_vendor_juice_world(connection, request.form)


def checking_name_and_password_for_vendor_juice_world(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select vendor_password from vendor_details where vendor_password = %(password)s and shop_no = '1'",
        {'password': validation_data['password']})
    returned_cold = cursor.fetchall()
    cursor.execute(
        "update items set is_available = 'yes' WHERE type = 'cold'")

    cursor.close()
    if len(returned_cold) == 0:
        return render_template('welcome_page.html')
    else:
        return beverages_cold()


def beverages_cold():
    menu = database_connection_cold()
    items = []
    for row in menu:
        items.append(row[0])
    return render_template("jinja_cold.html", items=items)


def database_connection_cold():
    print("try is running")
    cursor = connection.cursor()
    cursor.execute("select name_of_items from items where is_available='yes' and type='cold'")
    record = cursor.fetchall()
    cursor.close()
    return record


@app.route('/update_cold', methods=['POST'])
def update_cold():
    return update_cold_availability_to_database(connection, request.form)


def update_cold_availability_to_database(connection, update_data):
    cursor = connection.cursor()
    array = tuple(update_data.keys())
    update_no = "update items set is_available = 'no' WHERE type = 'cold'"
    update_yes = "update items set is_available = 'yes' WHERE name_of_items  IN %s and type = 'cold'"
    cursor.execute(update_no)
    cursor.execute(update_yes, (array,))
    connection.commit()
    cursor.close()


@app.route('/juice_world_report')
def juice_world_report():
    return render_template('report_calculation_juice_world.html')


@app.route('/calculation_juice_world')
def calculation_juice_world():
    sum = calculation_juice()
    return render_template("display.html", items=sum)


def calculation_juice():
    cursor = connection.cursor()
    cursor.execute(
        "select sum(cost*count)from items inner join order_page on items.serial_id = order_page.serial_id where type = 'cold';")
    cost = cursor.fetchall()
    cursor.close()
    return cost











@app.route('/who_am_i_madras_coffee')
def who_am_i_madras_coffee():
    return render_template('who_am_i_madras_coffee.html')


@app.route('/employee_login_page_madras_coffee')
def employee_login_page_madras_coffee():
    return render_template('employee_login_page_madras_coffee.html')


# @app.route('/guest_login')
# def guest_login():
#     return render_template('guest_login.html')


@app.route('/vendor_page_madras_coffee')
def vendor_page_madras_coffee():
    return render_template('vendor_personal_page_madras_coffee.html')


@app.route('/vendor_login_page_madras_coffee')
def vendor_login_page_madras_coffee():
    return render_template('vendor_login_page_madras_coffee.html')


@app.route('/employee_validation_madras_coffee', methods=['POST'])
def employee_validation_madras_coffee():
    return checking_name_and_password_madras_coffee(connection, request.form)


def checking_name_and_password_madras_coffee(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select password from employee_details where password = %(password)s ",
        {'password': validation_data['password']})
    returned_hot = cursor.fetchall()
    cursor.execute(
        "update items set is_available = 'yes' WHERE type = 'hot'")

    cursor.close()
    if len(returned_hot) == 0:
        return render_template('welcome_page.html')
    else:
        return render_template('ordering_page.html')


@app.route('/vendor_validation_madras_coffee', methods=['POST'])
def vendor_validation_madras_coffee():
    return checking_name_and_password_for_vendor_madras_coffee(connection, request.form)


def checking_name_and_password_for_vendor_madras_coffee(connection, validation_data):
    cursor = connection.cursor()
    cursor.execute(
        "select vendor_password from vendor_details where vendor_password = %(password)s and shop_no = '2'",
        {'password': validation_data['password']})
    returned_cold = cursor.fetchall()
    cursor.close()
    if len(returned_cold) == 0:
        return render_template('welcome_page.html')
    else:
        return beverages_hot()


def beverages_hot():
    menu = database_connection_hot()
    items = []
    for row in menu:
        items.append(row[0])
    return render_template("jinja_hot.html", items=items)


def database_connection_hot():
    print("try is running")
    cursor = connection.cursor()
    cursor.execute("select name_of_items from items where is_available='yes' and type='hot'")
    record = cursor.fetchall()
    cursor.close()
    return record


@app.route('/update_hot', methods=['POST'])
def update_hot():
    return update_hot_availability_to_database(connection, request.form)


def update_hot_availability_to_database(connection, update_data):
    cursor = connection.cursor()
    array = tuple(update_data.keys())
    update_no = "update items set is_available = 'no' WHERE type='hot'"
    update_yes = "update items set is_available = 'yes' WHERE name_of_items  IN %s and type='hot'"
    cursor.execute(update_no)
    cursor.execute(update_yes, (array,))
    connection.commit()
    cursor.close()


@app.route('/madras_coffee_report')
def madras_coffee_report():
    return render_template('report_calculation_madras_coffee.html')


@app.route('/calculation_madras_coffee')
def calculation_madras_coffee():
    sum = calculation_hot()
    return render_template("display.html", items=sum)


def calculation_hot():
    cursor = connection.cursor()
    cursor.execute(
        "select sum(cost*count)from items inner join order_page on items.serial_id = order_page.serial_id where type = 'hot';")
    cost = cursor.fetchall()
    cursor.close()
    return cost


if __name__ == '__main__':
    app.run(debug=True)
