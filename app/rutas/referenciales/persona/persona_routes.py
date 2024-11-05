from flask import Blueprint, render_template

persomod = Blueprint('persona', __name__, template_folder='templates')

@persomod.route('/persona-index')
def personaIndex():
    return render_template('persona-index.html')

