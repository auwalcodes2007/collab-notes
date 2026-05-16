from flask import render_template
from flask_login import login_required
from app.notes import notes_bp

@notes_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('notes/dashboard.html')