from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/sgx'
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

@app.route("/")
@app.route("/home")
def home():
    
    return render_template('home.html')

@app.route("/about")
def about():
    students = Student.query
    return render_template('about.html', students = students)

if __name__ == '__main__':
    app.run(debug=True)