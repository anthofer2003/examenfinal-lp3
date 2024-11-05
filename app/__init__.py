from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.persona.persona_routes import persomod
from app.rutas.referenciales.estudiante.estudiante_routes import estumod
from app.rutas.referenciales.profesor.profesor_routes import profemod
from app.rutas.referenciales.facultad.facultad_routes import facumod
from app.rutas.referenciales.carrera.carrera_routes import carremod
from app.rutas.referenciales.examen.examen_routes import examod
from app.rutas.referenciales.certificado.certificado_routes import certimod
from app.rutas.referenciales.turno.turno_routes import turmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(persomod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(estumod, url_prefix=f'{modulo0}/estudiante')
app.register_blueprint(profemod, url_prefix=f'{modulo0}/profesor')
app.register_blueprint(facumod, url_prefix=f'{modulo0}/facultad')
app.register_blueprint(carremod, url_prefix=f'{modulo0}/carrera')
app.register_blueprint(examod, url_prefix=f'{modulo0}/examen')
app.register_blueprint(certimod, url_prefix=f'{modulo0}/certificado')
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')

# importar gestionar compras
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedido_compras_routes \
    import pdcmod

# registro de modulos - gestionar compras
modulo1 = '/gestionar-compras'
app.register_blueprint(pdcmod, url_prefix=f'{modulo1}/registrar-pedido-compras')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedido_compras_api \
    import pdcapi
from app.rutas.referenciales.pais.pais_api import paisapi
from app.rutas.referenciales.persona.persona_api import persona_api
from app.rutas.referenciales.estudiante.estudiante_api import estudiante_api
from app.rutas.referenciales.profesor.profesor_api import profesor_api
from app.rutas.referenciales.facultad.facultad_api import facultad_api
from app.rutas.referenciales.carrera.carrera_api import carrera_api
from app.rutas.referenciales.examen.examen_api import tipo_examen_api
from app.rutas.referenciales.certificado.certificado_api import tipocertificado_api
from app.rutas.referenciales.turno.turno_api import turno_api

# APIS v1
apiversion1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=apiversion1)
app.register_blueprint(sucapi, url_prefix=apiversion1)
app.register_blueprint(paisapi, url_prefix=apiversion1)
app.register_blueprint(persona_api, url_prefix=apiversion1)
app.register_blueprint(estudiante_api, url_prefix=apiversion1)
app.register_blueprint(profesor_api, url_prefix=apiversion1)
app.register_blueprint(facultad_api, url_prefix=apiversion1)
app.register_blueprint(carrera_api, url_prefix=apiversion1)
app.register_blueprint(tipo_examen_api, url_prefix=apiversion1)
app.register_blueprint(tipocertificado_api, url_prefix=apiversion1)
app.register_blueprint(turno_api, url_prefix=apiversion1)

# Gestionar compras API
app.register_blueprint(pdcapi, url_prefix=f'{apiversion1}/{modulo1}/registrar-pedido-compras')