from flask import Blueprint, render_template, redirect, url_for, session
from flask_socketio import emit
from .network_scan import scan_network_devices
from flask import request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard')
def dashboard():
    devices = scan_network_devices()
    return render_template('dashboard.html', devices=devices)

@main_bp.route('/device/<ip>')
def device_detail(ip):
    return render_template('device_detail.html', device_ip=ip)
