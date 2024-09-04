from flask import Blueprint, render_template

ciumod = Blueprint('ciudad', __name__, template_folder='templates')

@ciumod.route('/ciudad-index')
def ciudadIndex():
    return render_template('ciudad-index.html')

@ciumod.route('/ciudad-agregar')
def ciudadAgregar():
    return render_template('ciudad-agregar.html')