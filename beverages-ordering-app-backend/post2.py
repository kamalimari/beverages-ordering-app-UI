import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def __init__(self, nam, employee_id):
    self.nam = nam
    self.employee_id = employee_id


def __repr__(self):
    return '<User %r>' % self.nam


@app.route('/')
def index():
    return render_template('add_user.html')


@app.route('/post-user', methods=['POST'])
def post_user():
    name = request.form['nam']
    employee_id = request.form['employee_id']
    connection = psycopg2.connect(user="admin", host="127.0.0.1", port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    cursor.execute("insert into employee_details values ('{}',{})".format(name, int(employee_id)))
    connection.commit()
    cursor.close()
    connection.close()
    return "Hello world"


if __name__ == '__main__':
    app.run()
