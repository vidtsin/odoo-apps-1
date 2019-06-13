# coding: utf-8

from odoo import fields, models

class OoGenre(models.Model):
    _name = 'oo.genre'
    _rec_name = 'name'

    name = fields.Char(string="Nom")
