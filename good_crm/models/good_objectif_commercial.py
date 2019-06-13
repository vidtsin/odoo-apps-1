# coding: utf-8

from odoo import models, fields, api


class ObjectifCommercial(models.Model):
    _name = 'good.crm.objectif.commercial'
    _rec_name = 'num'

    num = fields.Char()
    date = fields.Date()
    commercial_id = fields.Many2one(
        comodel_name='res.users',
        string='Commercial'
    )
    state = fields.Selection(
        selection=[
            ('init', 'En Cours'),
            ('valider', 'Valider'),
            ('annuler', 'Annuler'),
            ('reussi', 'Objectif Réussi'),
            ('echec', 'Objectif Échouer')
        ],
        default='init',
        string='Statut'
    )
    objectif_commercial_ids = fields.One2many(
        comodel_name='good.crm.objectif.commercial.line',
        inverse_name='objectif_id'
    )

    @api.one
    def valider_objectif(self):
        self.write({'state': 'valider'})

    @api.one
    def annuler_objectif(self):
        self.write({'state': 'annuler'})
