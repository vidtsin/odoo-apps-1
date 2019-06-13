# coding:utf-8

{
    'name': 'Odoo for library',
    'version': '0.1',
    'category': 'Warehouse',
    'description': """
    Odoo for library

    Odoo module for library management.

    Features

    - Consulting functions
    - Acquisition functions (purchase suggestions, orders and receipt of
    documents, pre-cataloging, and suppliers).
    - The functions of management of printed periodicals: management of
    subscriptions and states of collection, reception of numbers received;
    this function is closely related to the acquisitions module for everything
    related to subscription management.
    - Bibliographic control functions: management of the description of the
    collections (including the description of documents, copies, so-called
    authorities entities, etc.), particularly by manual import or cataloging;
    - Circulation functions: loan management, loan extensions, user bookings
    and orders, delays (reminders, suspensions or fines for late readers), user
    data
    - Statistics functions: reporting on the use of the system and the data it
    contains
    """,
    'author': 'Abdou Nasser',
    'email': 'abdounasser202@gmail.com',
    'website': 'https://www.nasserzone.com/',
    'depends': ['base', 'sale_management', 'purchase', 'stock'],
    'data': [
        'data/menu.xml',
        'views/oo_consultation_view.xml' 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
