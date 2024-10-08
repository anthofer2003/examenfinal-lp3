from flask import Blueprint, render_template

producmod = Blueprint('producto', __name__, template_folder='templates')

@producmod.route('/producto-index')
def productoIndex():
    return render_template('producto-index.html')

