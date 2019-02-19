import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
connection = psycopg2.connect(user="admin", host="127.0.0.1", port="5432", database="postgres")


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
    posting_data(connection, request.form)


if __name__ == '__main__':
    app.run()
