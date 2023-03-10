{
    'name': 'Concesionario',
    'version': '1.0',
    'summary': 'Módulo para la gestión de un concesionario',
    'description': """
        Este módulo permite la creación, modificación y/o borrado de vehículos en un concesionario, as.
    """,
    'website': 'https://github.com/a22adrianct/Modulo_SXE',
    'author': 'Adrián Cervera',
    'category': 'Sales',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_view.xml',
        'views/buyer_view.xml',
        'views/sale_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}
