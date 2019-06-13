from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'

    is_prospect = fields.Boolean()
