from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app.notes import notes_bp


# TODO: GET all notes 
@notes_bp.route('/dashboard')
@login_required
def dashboard():
    # Query database to get all notes
    notes = ''
    return render_template('notes/dashboard.html', notes=notes)

# TODO: Get create/ to create notes AND Post create/ to submit created note
@notes_bp.route('/create', methods=["GET", "POST"])
@login_required
def create_note():
    if request.method == "POST":
        # Create note here and add to db
        return redirect(url_for('notes.dashboard'))
    return render_template("notes/create.html")

# TODO: Get edit/ with note id to edit notes AND Post edit/ to submit editted note
@notes_bp.route('/edit/<int:id>', methods=["GET", "POST"])
@login_required
def edit_note(id):
    # Query database for note to edit using id
    note = ''
    return render_template("notes/edit.html", note=note)

# TODO: Get delete/ with note id to delete note
@notes_bp.route('/delete/<int:id>', methods=["POST"])
@login_required
def delete_note(id):
    # Query database for note to delete using id
    note = ''
    return redirect(url_for('notes.dashboard'))