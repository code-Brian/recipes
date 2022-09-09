from flask_app import app
from flask_app.models.user import User
from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/login')
def r_login():
    print('rendering login page...')
    return render_template('login.html')

@app.route('/success')
def r_success():

    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    print('rendering success page...')
    return render_template('success.html')

@app.route('/user/register', methods=['POST'])
def f_register_user():

    if not User.validate_registration(request.form):
        session['first_name'] = request.form.get('first_name')
        session['last_name'] = request.form.get('last_name')
        session['email'] = request.form.get('email')

        return redirect('/login')

    session.clear()

    pw_hash = bcrypt.generate_password_hash(request.form.get('password'))
    print(pw_hash)

    data = {
        'first_name': request.form.get('first_name'),
        'last_name' : request.form.get('last_name'),
        'email' : request.form.get('email'),
        'password' : pw_hash
    }

    user_id = User.save(data)

    session['user_id'] = user_id

    return redirect('/success')

@app.route('/user/login', methods=['POST'])
def f_user_login():
    print('Attempting to login...')

    data = {
        'email' : request.form.get('email')
    }

    user_match = User.get_user_email(data)

    if not user_match:
        flash(u'Invalid Email/Password', 'login')
        return redirect('/login')
    
    if not bcrypt.check_password_hash(user_match.password, request.form.get('password')):
        flash(u'Invalid Email/Password', 'login')
        return redirect('/login')

    session['user_id'] = user_match.id
    session['first_name'] = user_match.first_name.capitalize()
    session['last_name'] = user_match.last_name.capitalize()

    return redirect('/success')

@app.route('/logout')
def b_logout():
    print('clearing the session and logging out...')
    session.clear()
    return redirect('/login')
