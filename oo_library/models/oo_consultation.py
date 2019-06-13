# coding: utf-8

from odoo import fields, models

class OoConsultation(models.Model):
    _name = 'oo.consultation'
    _rec_name = 'titre'

    titre = fields.Char()
    auteur_id = fields.Many2one(
        comodel_name='res.users',
        string='Auteur'
    )
    genre_id = fields.Many2one(
        comodel_name='oo.genre',
        string='Genre'
    )
    editeur_id = fields.Many2one(
        comodel_name='res.partner',
        string='Éditeur'
    )
    collection_id = fields.Many2one(
        comodel_name='oo.collection',
        string='Collection'
    )
    resume = fields.Text(string="Résumé")
    code_isbn = fields.Char(string='Code ISBN')
