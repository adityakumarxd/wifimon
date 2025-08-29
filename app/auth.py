from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.get_user(username)  
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', category='error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        db.add_user(username, hashed_password)  
        flash('Registration successful! You can now log in.', category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html') 