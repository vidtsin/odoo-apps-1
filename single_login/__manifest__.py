##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2013 OpenERP S.A. (<http://openerp.com>).
#
#    Copyright (C) 2011-2015 Nevpro Business Solutions Pvt Ltd. (<http://www.nevpro.co.in>).
#
#    Copyright (C) 2019 Abdou Nasser (<http://www.nasser.cm>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': 'Odoo Single Login',
	'price': 87
    'currency': 'EUR',
    "images": ['images/undraw_hacker_mind_6y85.png'],
	'version': '0.0.1',
	'category': 'Extra Tools',
	'sequence': 1,
	'summary': 'Prevent multiple login for the same user in Odoo 10+.',
	'description': """
Prevent multiple login for the same user
=======================================

Module to restrict multiple sign in for the same user in Odoo 10 and higher""",
	'author': 'Abdou Nasser',
	"support": "abdounasser202@gmail.com",
	'website': 'http://www.nasser.cm',
	"license": "AGPL-3",
	'depends': ['web','base'],
	'data': [
		'views/single_login.xml',
		'views/custom_template.xml',
		'scheduler.xml',
		],
	'demo_xml': [],
	'installable': True,
	'application': True,
	'auto_install': False,
}
