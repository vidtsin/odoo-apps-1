{
    "name": "Sales People Objectives and Evaluation",
    "summary": "Assign objectives to salespeople and evaluate them",
    "category": "Sales",
    'price': 35,
    'currency': 'EUR',
    "images": ['images/undraw_segmentation_uioo.png'],
    "version": "0.0.2",
    "author": "Abdou Nasser",
    "support": "abdounasser202@gmail.com",
    "website": "https://formation-odoo.blogspot.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "crm",
        "sale_crm",
        "web_notify"
    ],
    "data": [
        'data/menu.xml',
        'views/objectif_commercial_view.xml',
        'views/res_partner.xml',
        'views/pipeline.xml',
        'views/activities.xml',
        'views/dashboard.xml',
        'views/quotations.xml',
        'wizards/evaluer_objectif.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
