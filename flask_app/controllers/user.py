from flask_app import app
from flask_app.models.users import User
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


@app.route('/')
def r_landing():
    return render_template('landing.html')


@app.route('/submit', methods=['POST'])
def f_submit():
    inbound = request.form
    if inbound.get('submit_mode') == 'register':
        if User.validate_registration(inbound):
            pw_hash = bcrypt.generate_password_hash(inbound.get('password'))
            data = {
                'first_name': inbound.get('first_name'),
                'last_name': inbound.get('last_name'),
                'email': inbound.get('email'),
                'password': pw_hash
            }

            user_id = User.create_user(data)
            session['user_id'] = user_id

            return redirect('/wall')
        else:
            return redirect('/')
    else:
        if User.validate_login(inbound):
            data = {
                'email': inbound.get('email')
            }
            user_in_db = User.find_by_email(data)

            if not user_in_db:
                flash('Invalid Email/Password')
                return redirect('/')
            if not bcrypt.check_password_hash(user_in_db.password, inbound.get('password')):
                flash('Invalid Email/Password')
                return redirect('/')
            
            session['user_id'] = user_in_db.id
            return redirect('/wall')
        else:
            return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')