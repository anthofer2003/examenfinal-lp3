from flask import Blueprint, render_template

facumod = Blueprint('facultad', __name__, template_folder='templates')

@facumod.route('/facultad-index')
def facultadIndex():
    return render_template('facultad-index.html')

