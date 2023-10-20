from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Importa las vistas y rutas específicas de administración aquí
from . import views

