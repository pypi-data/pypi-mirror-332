import os
from jinja2 import Template

def get_package_root():
    # Obtiene la ubicación absoluta del archivo actual
    current_file = os.path.abspath(__file__)
    # Determina el directorio raíz del paquete
    package_root = os.path.dirname(current_file)
    return package_root

def renderTemplate(templateName: str, fileName:str, render_params: dict) -> str:
    '''
    return content
    '''

    # Construir la ruta absoluta de la plantilla

    templates_dir = os.path.join(get_package_root(), '..', 'templates', templateName)
    templates_dir = os.path.normpath(templates_dir)  # Normalizar la ruta 

    # Cargar la plantilla imports
    template_imports = os.path.join(templates_dir, fileName)
    with open(template_imports, 'r') as template_file:
        template_content = template_file.read()

    # Renderizar la plantilla imports
    return Template(template_content).render(**render_params)


def create__init__file(path):
    """Crea un archivo __init__.py en el directorio especificado"""
    with open(os.path.join(path, '__init__.py'), 'w') as f:
        pass


def create__init__files(path):
    """Crea un archivo __init__.py en el directorio especificado 
    y en todos los directorios padres hasta el directorio raíz 
    o hasta encontrar un archivo __init__.py"""
    while True:
        if os.path.exists(os.path.join(path, '__init__.py')):
            break
        create__init__file(path)
        path = os.path.dirname(path)
        if path == '' or path == '/':
            break
