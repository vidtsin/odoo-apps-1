# -*- coding: utf-8 -*-

from openerp import fields, models

class StockAfaire(models.Model):
    _name = 'stock.affaire'

    nom = fields.Char("Nom", required=True)
    article = fields.Many2one("product.product", required=True)
