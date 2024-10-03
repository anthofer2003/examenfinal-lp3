from flask import Blueprint, render_template

estumod = Blueprint('estudiante', __name__, template_folder='templates')

@estumod.route('/estudiante-index')
def estudianteIndex():
    return render_template('estudiante-index.html')

