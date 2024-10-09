from flask import Blueprint, render_template

certimod = Blueprint('certificado', __name__, template_folder='templates')

@certimod.route('/certificado-index')
def certificadoIndex():
    return render_template('certificado-index.html')

