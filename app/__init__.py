from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from config import Config

# Database
from app.extensions import db

from pony.flask import Pony
from pony.orm import commit
from werkzeug.security import generate_password_hash

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Pony Database
    db.bind(**app.config["PONY"])
    db.generate_mapping()
    Pony(app)

    # Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return db.Cuenta.get(id=user_id)

    # Register blueprints (modules)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.asistencia import bp as asistencia_bp
    app.register_blueprint(asistencia_bp, url_prefix='/asistencia')
    from app.caja import bp as caja_bp
    app.register_blueprint(caja_bp, url_prefix='/caja')
    from app.config import bp as config_bp
    app.register_blueprint(config_bp, url_prefix='/config')
    from app.gestion import bp as gestion_bp
    app.register_blueprint(gestion_bp, url_prefix='/gestion')
    from app.inscripcion import bp as inscripcion_bp
    app.register_blueprint(inscripcion_bp, url_prefix='/inscripcion')
    from app.reporte import bp as reporte_bp
    app.register_blueprint(reporte_bp, url_prefix='/reporte')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        if request.method == 'POST':
            user =  db.Cuenta.get(nombre=request.form['nombre'])
            if user and user.check_password(request.form['contrasena']):
                login_user(user, remember=True)
                return redirect(url_for('main.index'))
            else:
                flash("Nombre o contraseña no válido")
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        if request.method == 'POST':
            succesful = True
            if db.Cuenta.get(nombre=request.form['nombre']):
                flash("Ese nombre ya existe")
                succesful = False
            if db.Cuenta.get(correo=request.form['correo']):
                flash("Ese correo ya está en uso")
                succesful = False
            if request.form['contrasena'] != request.form['contrasena-repeat']:
                flash("Ambas contraseñas deben ser iguales")
                succesful = False
            if succesful:
                newUser = db.Cuenta(nombre=request.form['nombre'],
                                    contrasena=generate_password_hash(request.form['contrasena']),
                                    correo=request.form['correo'],
                                    rol="ninguno")
                commit()
                login_user(newUser, remember=True)
                return redirect(url_for('main.index'))
        return render_template('register.html')
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('main.index'))
    
    @app.route('/cuenta')
    @login_required
    def cuentaInfo():
        flash(current_user.rol)
        return redirect(url_for('main.index'))

    return app