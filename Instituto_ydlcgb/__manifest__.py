# -*- coding: utf-8 -*-
{
    'name': "InstitutoYDLCGB",

    'summary': "Aqui estudia gente buena.",

    'description': """
Esto es pa estudiar, el que venga a hacer el tonto a casa.
    """,

    'author': "Yo Yeray de la Cruz Garcia Bravo",
    'website': "https://theuselessweb.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/viewprofesor.xml',
        'views/viewalumno.xml',
        'views/viewciclo.xml',
        'views/viewmodulo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

