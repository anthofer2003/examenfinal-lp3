from flask import Blueprint, render_template

asigmod = Blueprint('asignatura', __name__, template_folder='templates')

@asigmod.route('/asignatura-index')
def asignaturaIndex():
    return render_template('asignatura-index.html')

