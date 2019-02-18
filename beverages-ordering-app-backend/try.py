import psycopg2
from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def entry():

    print("try is running")
    connection = psycopg2.connect(user="admin", host="127.0.0.1", port="5432",
                                      database="postgres")
    cursor = connection.cursor()
    cursor.execute("insert into employee_details values("record = cursor.fetchall()

    return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


hello()

if __name__ == '__main__':
    app.run()