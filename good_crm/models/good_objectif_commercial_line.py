# coding: utf-8

from odoo import models, fields


class ObjectifCommercialLine(models.Model):
    _name = 'good.crm.objectif.commercial.line'

    client_id = fields.Many2one(
        comodel_name='res.partner',
        string='Client'
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Produit'
    )
    nbre_vente = fields.Integer()
    chiffre_affaire = fields.Integer()
    objectif_id = fields.Many2one(
        comodel_name='good.crm.objectif.commercial'
    )
