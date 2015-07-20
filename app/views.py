from app import app
from flask import render_template
from backend import increase_count

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<StudentID>')
def user_details(StudentID):
    user = {'id' : StudentID}
    return render_template('user.html', user=user, result=increase_count(StudentID))
