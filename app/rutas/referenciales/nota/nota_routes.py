from flask import Blueprint, render_template

notamod = Blueprint('nota', __name__, template_folder='templates')

@notamod.route('/nota-index')
def notaIndex():
    return render_template('nota-index.html')

