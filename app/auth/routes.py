from flask import render_template, redirect, url_for, flash, request
from app.auth import auth_bp
from app.extensions import db, bcrypt
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("notes.dashboard"))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user already exists
        existing_user = db.session.execute(
            db.select(User).where(User.email==email)
            ).scalar_one_or_none()
        
        if existing_user: 
            flash("Email already registered.", 'error')
            return redirect(url_for("auth.register"))

        # Hash password and create user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash("Account created successfully! Please log in", "success")
        return redirect(url_for('auth.login'))
    
    return render_template("auth/register.html")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('notes.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(db.select(User).where(User.email==email)).scalar_one_or_none()

        if not user or not bcrypt.check_password_hash(user.password, password):
            flash("Invalid email or password.", "error")
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('notes.dashboard'))
        
    return render_template("auth/login.html")


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
