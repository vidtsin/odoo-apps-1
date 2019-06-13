# -*- coding: utf-8 -*-
import datetime
import logging
from openerp import api, fields, models

_logger = logging.getLogger()

class SmsAccount(models.Model):

    _name = "sms.account"

    name = fields.Char(string='Account Name', required=True)
    account_gateway_id = fields.Many2one('sms.gateway', string="Account Gateway", required=True)
    gateway_model = fields.Char(string="Gateway Model", related="account_gateway_id.gateway_model_name")

    def send_message(self, from_number, to_number, sms_content,
        my_model_name='', my_record_id=0, media=None, queued_sms_message=None,
        media_filename=None):
        """Send a message from this account"""
        return self.env[self.gateway_model].send_message(self.id, from_number,
            to_number, sms_content, my_model_name, my_record_id, media,
            queued_sms_message, media_filename=media_filename)


    @api.model
    def check_all_messages(self):
        """Check for any messages that might have been missed during server downtime"""
        my_accounts = self.env['sms.account'].search([])
        for sms_account in my_accounts:
            self.env[sms_account.account_gateway_id.gateway_model_name].check_messages(
                sms_account.id)

    @api.model
    def send_sms_for_birthday(self):
        """Send a SMS from this account for birthday"""
        _logger.info("Sending SMS for birthdays")
        birthdays = self.env['res.partner'].search([
            ('birthday', '=', datetime.date.today())
        ])
        if birthdays:
            sms_tmp = self.env['sms.template'].search([
                ('is_birthday', '=', True)
            ])
            a = sms_tmp.send_sms(sms_tmp.id,sms_tmp.id)
            _logger.info(str(a))
            return sms_tmp.send_sms(sms_tmp.id,sms_tmp.id)
