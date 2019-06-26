# coding:utf-8

{
    'name': 'Odoo for library management',
    "summary": "Odoo module for library management",
    'category': 'Document Management',
    # 'price': 35,
    # 'currency': 'EUR',
    "images": ['images/undraw_books_6rhq.png'],
    'version': '0.0.2',
    "author": "Abdou Nasser",
    "support": "abdounasser202@gmail.com",
    "website": "https://formation-odoo.blogspot.com",
    "license": "LGPL-3",
    'depends': ['base', 'sale_management', 'purchase', 'stock'],
    'data': [
        'data/menu.xml',
        'views/oo_consultation_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
