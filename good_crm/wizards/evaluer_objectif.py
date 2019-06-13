# coding: utf-8

from odoo import models, api, fields

class WizardEvaluerObjectif(models.Model):
    _name = 'good.crm.wizard.evaluer.objectif'

    date = fields.Date()
    chiffre_affaire = fields.Integer(string="Chiffre réalisé")
    commercial_id = fields.Many2one("res.users")
    client_id = fields.Many2one("res.partner")

    @api.multi
    def evaluer_objectif(self):
        ir_model_data = self.env['ir.model.data']
        objectifs_tree = ir_model_data.get_object_reference(
        'good_crm_crm_commercial', 'good_crm_objectif_commercial_view_tree')[1]

        return self.env.user.notify_info(
            'Évaluation des objectifs en cours...',
            title='Évaluation'
        )
