# coding: utf-8

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    book_id = fields.Many2one('oo.consultation', string="Livre associé")
