import pyodbc
from flask import Flask, render_template, request, redirect, url_for
from blueprints import admin_bp
from config import DevelopmentConfig  
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.register_blueprint(admin_bp)
app.config.from_object(DevelopmentConfig)  


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\\Users\\SENA\\Music\\Parcial2\\TasksDB.accdb;'
)


def connect_db():
    return pyodbc.connect(conn_str)


@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TasksDB')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_description = request.form['task_description']
        task_status = request.form['task_status']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TasksDB (Descripción, Estado) VALUES (?, ?)', (task_description, task_status))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




