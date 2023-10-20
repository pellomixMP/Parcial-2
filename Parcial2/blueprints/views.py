
from flask import render_template
from . import admin_bp
from models.tarea import User  

@admin_bp.route('/')
def admin_home():
    return render_template('admin/home.html')

@admin_bp.route('/users')
def admin_users():
    # Lógica para administrar usuarios
    return render_template('admin/users.html')

