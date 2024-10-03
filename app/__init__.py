from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.estudiante.estudiante_routes import estumod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(estumod, url_prefix=f'{modulo0}/estudiante')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.persona.persona_api import perapi
from app.rutas.referenciales.estudiante.estudiante_api import estudiante_api

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(nacioapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(perapi, url_prefix=version1)
app.register_blueprint(estudiante_api, url_prefix=version1)