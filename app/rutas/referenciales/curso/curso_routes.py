from flask import Blueprint, render_template

curmod = Blueprint('curso', __name__, template_folder='templates')

@curmod.route('/curso-index')
def cursoIndex():
    return render_template('curso-index.html')

