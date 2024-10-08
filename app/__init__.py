from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.estudiante.estudiante_routes import estumod
from app.rutas.referenciales.programa.programa_routes import promod
from app.rutas.referenciales.profesor.profesor_routes import profemod
from app.rutas.referenciales.matricula.matricula_routes import matmod
from app.rutas.referenciales.nota.nota_routes import notamod
from app.rutas.referenciales.horario.horario_routes import hormod
from app.rutas.referenciales.evaluacion.evaluacion_routes import evamod
from app.rutas.referenciales.asignatura.asignatura_routes import asigmod
from app.rutas.referenciales.producto.producto_routes import producmod
from app.rutas.referenciales.curso.curso_routes import curmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(estumod, url_prefix=f'{modulo0}/estudiante')
app.register_blueprint(promod, url_prefix=f'{modulo0}/programa')
app.register_blueprint(profemod, url_prefix=f'{modulo0}/profesor')
app.register_blueprint(matmod, url_prefix=f'{modulo0}/matricula')
app.register_blueprint(notamod, url_prefix=f'{modulo0}/nota')
app.register_blueprint(hormod, url_prefix=f'{modulo0}/horario')
app.register_blueprint(evamod, url_prefix=f'{modulo0}/evaluacion')
app.register_blueprint(asigmod, url_prefix=f'{modulo0}/asignatura')
app.register_blueprint(producmod, url_prefix=f'{modulo0}/producto')
app.register_blueprint(curmod, url_prefix=f'{modulo0}/curso')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.persona.persona_api import perapi
from app.rutas.referenciales.estudiante.estudiante_api import estudiante_api
from app.rutas.referenciales.programa.programa_api import programa_api
from app.rutas.referenciales.profesor.profesor_api import profesorapi
from app.rutas.referenciales.matricula.matricula_api import matricula_api
from app.rutas.referenciales.nota.nota_api import notaapi
from app.rutas.referenciales.horario.horario_api import horarios_api
from app.rutas.referenciales.evaluacion.evaluacion_api import evaluacion_api
from app.rutas.referenciales.asignatura.asignatura_api import asignatura_api
from app.rutas.referenciales.producto.producto_api import producto_api
from app.rutas.referenciales.curso.curso_api import cursos_api

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(nacioapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(perapi, url_prefix=version1)
app.register_blueprint(estudiante_api, url_prefix=version1)
app.register_blueprint(programa_api, url_prefix=version1)
app.register_blueprint(profesorapi, url_prefix=version1)
app.register_blueprint(matricula_api, url_prefix=version1)
app.register_blueprint(notaapi, url_prefix=version1)
app.register_blueprint(horarios_api, url_prefix=version1)
app.register_blueprint(evaluacion_api, url_prefix=version1)
app.register_blueprint(asignatura_api, url_prefix=version1)
app.register_blueprint(producto_api, url_prefix=version1)
app.register_blueprint(cursos_api, url_prefix=version1)