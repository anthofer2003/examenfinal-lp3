from flask import Blueprint, render_template

promod = Blueprint('programa', __name__, template_folder='templates')

@promod.route('/programa-index')
def programaIndex():
    return render_template('programa-index.html')

