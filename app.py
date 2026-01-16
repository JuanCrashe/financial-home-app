import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')

# --- Public Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

# --- Dashboard Routes ---

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

@app.route('/dashboard/ingresos')
def ingresos():
    return render_template('dashboard/ingresos.html')

@app.route('/dashboard/egresos')
def egresos():
    return render_template('dashboard/egresos.html')

@app.route('/dashboard/presupuestos')
def presupuestos():
    return render_template('dashboard/presupuestos.html')

@app.route('/dashboard/reportes')
def reportes():
    return render_template('dashboard/reportes.html')

@app.route('/dashboard/configuracion')
def configuracion():
    return render_template('dashboard/configuracion.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
