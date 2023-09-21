FLASK:

Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

What is Flask vs Django:

Flask vs Django in 2023: Which One to Choose and When?
Flask and Django are both open-source Python-based web development frameworks designed to ease code complexity for developers. While Django is a full-stack framework, Flask is famous as a micro-framework that is light-weight but extensible.


Install Flask:
Install Flask and any other necessary dependencies:
pip install Flask
Create Your Flask App:
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
Run the Flask App:
python app.py
Install Required Dependencies:
pip install Flask SQLAlchemy pymysql
2. Set Up Your Flask Application:
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
db = SQLAlchemy(app)
3. Create a User Model:
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
4. Create Database Tables:

Run the following command to create the database tables based on the defined models:

python
>>> from app import db
>>> db.create_all()
>>> exit()
5. Create Routes for /users and /new_user:

Implement routes to list existing users and add new users.

python

# app.py

from flask import render_template, redirect, url_for
from models import User

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('users'))
    
    return render_template('new_user.html')
6. Create HTML Templates:

Create HTML templates for listing users and adding new users.

html

<!-- templates/users.html -->

<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
                <tr>
                    <td>{{ user.id }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="{{ url_for('new_user') }}">Add New User</a>
</body>
</html>
html
Copy code
<!-- templates/new_user.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Add New User</title>
</head>
<body>
    <h1>Add New User</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required><br>
        <label for="email">Email:</label>
        <input type="email" name="email" required><br>
        <input type="submit" value="Add User">
    </form>
    <a href="{{ url_for('users') }}">Back to User List</a>
</body>
</html>
7. Run the Flask App:

Run your Flask application:
python app.py
1. Modify the Route:

# app.py

from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
db = SQLAlchemy(app)

@app.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)  # User not found, raise a 404 error.
    
    return render_template('user_details.html', user=user)

# ...other routes...
2. Create an HTML Template for User Details:

Create an HTML template (user_details.html) to display the user's details.

html
Copy code
<!-- templates/user_details.html -->

<!DOCTYPE html>
<html>
<head>
    <title>User Details</title>
</head>
<body>
    <h1>User Details</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
            </tr>
        </tbody>
    </table>
    <a href="{{ url_for('users') }}">Back to User List</a>
</body>
</html
3. Create an Error Handling Route

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom 404 error page
@app.route('/not_found')
def not_found():
    return render_template('404.html'), 404
4. Create an HTML Template for 404 Error:

Create an HTML template (404.html) for the custom 404 error page.

html
Copy code
<!-- templates/404.html -->

<!DOCTYPE html>
<html>
<head>
    <title>404 - Not Found</title>
</head>
<body>
    <h1>404 - Not Found</h1>
    <p>The resource you are looking for does not exist.</p>
    <a href="{{ url_for('users') }}">Back to User List</a>
</body>
</html>
5. Run the Flask App:

Run your Flask application:
python app.p

SQL:
SQL stands for Structured Query Language
SQL lets you access and manipulate databases
SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987
SQL can execute queries against a database
SQL can retrieve data from a database
SQL can insert records in a database
SQL can update records in a database
SQL can delete records from a database
SQL can create new databases
SQL can create new tables in a database



1. Create the MySQL Database:
CREATE DATABASE users;
2. Use the Database:
USE users;
3. Create the "users" Table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(255)
);

4. Verify the Table:
DESCRIBE users;
1. Insert Sample Data into the "users" Table:
-- Inserting sample data into the "users" table
INSERT INTO users (name, email, role) VALUES
    ('John Doe', 'john@example.com', 'Admin'),
    ('Jane Smith', 'jane@example.com', 'User');
This query inserts two users into the "users" table, providing values for the name, email, and role columns.

2. Retrieve All Users from the "users" Table:

SELECT * FROM users;

-- Retrieve all users from the "users" table
SELECT * FROM users;
sql
-- Retrieve a specific user by their ID (e.g., ID=1)
SELECT * FROM users WHERE id = 1002;








