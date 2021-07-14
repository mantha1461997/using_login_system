from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo



app = Flask(__name__)
app.secret_key = b'\xb0\x05t\xa6z\xba\xb6n\x93\xabzf\x93{\xceq'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.using_login_system

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ =="__main__":
    app.run(debug=True)