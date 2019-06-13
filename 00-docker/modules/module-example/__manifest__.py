# -*- coding: utf-8 -*-

""" On commence par creer ce fichier """ 

{
    'name': 'OdooModule',
    'version': '0.1',
    'category': 'Website',
    'description': """ Petit exemple qui présente comment on fais un module
    sur Odoo """,
    'author': 'Abdou Nasser',
    'website': 'http://lastoredenasserzone.appspot.com'
    'depends': ['base'],
    'data': ['odoo_module.xml'],
    'installable': True,
    'auto_install': False,
}