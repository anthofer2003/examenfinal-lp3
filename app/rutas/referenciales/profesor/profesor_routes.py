from flask import Blueprint, render_template

profemod = Blueprint('profesor', __name__, template_folder='templates')

@profemod.route('/profesor-index')
def profesorIndex():
    return render_template('profesor-index.html')

