from flask import Blueprint, render_template

evamod = Blueprint('evaluacion', __name__, template_folder='templates')

@evamod.route('/evaluacion-index')
def evaluacionIndex():
    return render_template('evaluacion-index.html')

