


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import Sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
db = SQLAlchemy(app)
from flask import render_template, redirect, url_for
from models import User

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom 404 error page
@app.route('/not_found')
def not_found():
    return render_template('404.html'), 404
        username = request.form['username']
        email = request.form['email']
        
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('users'))
    
    return render_template('new_user.html')
