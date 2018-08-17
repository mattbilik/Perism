from flask import Flask as fl , render_template as rt, request, flash, redirect, url_for, session, logging
from coursedata import Courses
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps


app = fl(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'leiakkk4545'
app.config['MYSQL_DB'] = 'perism'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3306

#init MySQL
mysql = MySQL(app)

Courses = Courses()
app.debug = True
@app.route('/')
def index():
    return rt('index.html')



class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',[
    validators.EqualTo('confirm', message="Passwords don't match."),
    validators.DataRequired()
    ])
    confirm = PasswordField('Confirm Password')


# check if user is logged if __name__ == '__main__':


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)", (name, email, username, password))
        #commit
        mysql.connection.commit()
        #close
        cur.close()
        flash('You are now registered and can log in.', 'success')
        return redirect(url_for('login'))
    return rt('register.html', form=form)

    # user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        app.logger.info('posted!')

        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            app.logger.info('TABLE exists')
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are logged in.', 'success')
                return redirect(url_for('appy'))
            else:
                error = "Invalid login"
                return rt('login.html', error=error)
                cur.close()
        else:
            error = "Username not found"
            return rt('login.html', error=error)

    app.logger.info('Closed')
    return rt('login.html')
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login.', 'danger')
            return redirect(url_for('login'))
    return wrap
@app.route('/logout')
def logout():
    session.clear()
    flash('You are logged out', 'success')
    return redirect(url_for('index'))

    #acc app
@app.route('/app')
@is_logged_in
def appy():
    return rt('app.html', courses = Courses)

if __name__ == '__main__':
    app.secret_key='GingerfuckyoU124!'
    app.run()
