from flask import Blueprint, render_template

carremod = Blueprint('carrera', __name__, template_folder='templates')

@carremod.route('/carrera-index')
def carreraIndex():
    return render_template('carrera-index.html')

