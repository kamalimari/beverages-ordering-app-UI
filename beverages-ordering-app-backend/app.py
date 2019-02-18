import psycopg2
from flask import Flask
 app = Flask(__name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


def __init__(self, username, email):
        self.username = username
        self.email = email


def __init__(self):
    return '<User %r>' % self.username


@app.route('/')
def index():
    return 'add_user.html'


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    app.run()


