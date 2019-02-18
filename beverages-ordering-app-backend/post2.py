import psycopg2
from flask import Flask, render_template
import json
app = Flask(__name__)
 class User(db.postgres):













@app.route('/')
def index():
    return render_template('add_user.html')


@app.route('/post_user', methods=['POST'])












def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()


def database_connect():
    try:
        print("try is running")
        connection = psycopg2.connect(user="admin", host="127.0.0.1", port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        cursor.execute("select count (*) from employee_details")
        record = cursor.fetchall()

        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    app.run()