# coding: utf-8

from odoo import fields, models

class OoCollection(models.Model):
    _name = 'oo.collection'
    _rec_name = 'name'

    name = fields.Char(string="Nom")
