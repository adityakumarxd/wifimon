from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple hardcoded check - replace with router creds or DB
        if username == 'admin' and password == 'admin123':
            session['user'] = username
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
