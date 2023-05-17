from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


# создаем таблицу Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    link = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'


# создаем все таблицы
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/add', methods=['POST'])
def add_project():
    title = request.form['title']
    link = request.form['link']
    project = Project(title=title, link=link)
    db.session.add(project)
    db.session.commit()
    return 'Project added!'


if __name__ == '__main__':
    app.run(debug=True)