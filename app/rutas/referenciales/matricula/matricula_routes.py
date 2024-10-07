from flask import Blueprint, render_template

matmod = Blueprint('matricula', __name__, template_folder='templates')

@matmod.route('/matricula-index')
def matriculaIndex():
    return render_template('matricula-index.html')

