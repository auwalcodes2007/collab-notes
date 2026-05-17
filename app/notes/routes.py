from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.notes import notes_bp
from ..extensions import db
from ..models import Note


@notes_bp.route('/dashboard')
@login_required
def dashboard():
    notes = db.session.execute(
        db.select(Note).where(Note.user_id == current_user.id)
        ).scalars().all()
    return render_template('notes/dashboard.html', notes=notes)


@notes_bp.route('/create', methods=["GET", "POST"])
@login_required
def create_note():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        new_note = Note(title=title, content=content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note created.', 'success')
        return redirect(url_for('notes.dashboard'))
    return render_template("notes/create.html")


@notes_bp.route('/edit/<int:id>', methods=["GET", "POST"])
@login_required
def edit_note(id):
    note = db.session.get(Note, id)

    if not note or note.user_id != current_user.id:
        flash("Note not found.", "error")
        return redirect(url_for('notes.dashboard'))
    
    if request.method == "POST":
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.add(note)
        db.session.commit()
        flash("Note updated.", "success")
        return redirect(url_for('notes.dashboard'))
    
    return render_template("notes/edit.html", note=note)


@notes_bp.route('/delete/<int:id>', methods=["POST"])
@login_required
def delete_note(id):
    note = db.session.get(Note, id)
    if not note or note.user_id != current_user.id:
        flash("Note not found.", "error")
        return redirect(url_for('notes.dashboard'))
    
    db.session.delete(note)
    db.session.commit()

    flash("Note deleted.", "success")
    return redirect(url_for('notes.dashboard'))