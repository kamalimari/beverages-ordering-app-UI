import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from modules.posting_data_in_database import posting_data

app = Flask(__name__)
CORS(app)
connection = psycopg2.connect("dbname=postgres user=admin")


def __init__(self, nam, employee_id):
    self.nam = nam
    self.employee_id = employee_id


@app.route('/')
def index():
    return render_template('getting_data.html')


@app.route('/post-data', methods=['POST'])
def post_user():
    posting_data(connection, request.form)
    return render_template('display.html', shared=request.form)


if __name__ == '__main__':
    app.run()
