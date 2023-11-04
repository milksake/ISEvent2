from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from config import Config
from app.models.cuenta import Cuenta, users, get_user, get_user_from_email

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        for user in users:
            if user.id == user_id:
                return user
        return None

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
            user = get_user(request.form['nombre'])
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
            if get_user(request.form['nombre']):
                flash("Ese nombre ya existe")
                succesful = False
            if get_user_from_email(request.form['contrasena']):
                flash("Ese email ya está en uso")
                succesful = False
            if request.form['contrasena'] != request.form['contrasena-repeat']:
                flash("Ambas contraseñas deben ser iguales")
                succesful = False
            if succesful:
                newUser = Cuenta(str(len(users)), request.form['nombre'], request.form['contrasena'], request.form['correo'], "ninguno", None, None)
                users.append(newUser)
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