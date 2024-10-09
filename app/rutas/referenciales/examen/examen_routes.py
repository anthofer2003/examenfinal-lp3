from flask import Blueprint, render_template

examod = Blueprint('examen', __name__, template_folder='templates')

@examod.route('/examen-index')
def examenIndex():
    return render_template('examen-index.html')

