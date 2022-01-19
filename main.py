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


class Youtube(db.Model):
    __tablename__ = "youtube"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), unique=True, nullable=False)

db.create_all()


def embeded(link):
    ans = link.split('=')[1].split('&')[0]
    return f"https://www.youtube.com/embed/{ans}"

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/aboutme")
def aboutme():
    return render_template("about-me.html")


@app.route("/patents")
def patent():
    return render_template("patent.html")


@app.route("/publications")
def publications():
    puclications = {}
    data = db.session.query(BlogPost).all()
    n = 0
    for d in data:
        puclications[n] = [d.name, d.link]
        n += 1
    return render_template("publications.html", data=puclications)


@app.route('/youtube')
def youtube():
    all_data = {}
    data = db.session.query(Youtube).all()
    n = 0
    for d in data:
        all_data[n] = [d.name, embeded(d.link)]
        n += 1
    return render_template('youtube.html', data=all_data)


@app.route("/elements")
def elements():
    return render_template("elements.html")


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)