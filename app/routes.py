from flask import render_template, redirect, url_for, request, flash
from app import app
from app.auth import login_required
from app.network_scan import scan_network_devices
from app.traffic_sniffer import start_sniffer

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    devices = scan_network_devices()
    return render_template('dashboard.html', devices=devices)

@app.route('/device/<device_id>')
@login_required
def device_detail(device_id):
    traffic_logs = start_sniffer(device_id)
    return render_template('device_detail.html', device_id=device_id, traffic_logs=traffic_logs)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if authenticate_user(username, password):
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('home'))