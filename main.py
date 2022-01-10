from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    __tablename__ = "publications"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), unique=True, nullable=False)


db.create_all()


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/aboutme")
def aboutme():
    return render_template("about-me.html")


@app.route("/generic")
def generic():
    return render_template("generic.html")


@app.route("/elements")
def elements():
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True)