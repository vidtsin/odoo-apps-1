# -*- coding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2004-2013 odoo S.A. (<http://odoo.com>).
#
#    Copyright (C) 2011-2015 Nevpro Business Solutions Pvt Ltd. (<http://www.nevpro.co.in>).
#
#    Copyright (C) 2019 Abdou Nasser (<http://www.nasser.cm>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
import odoo
from odoo import fields, api, models
from datetime import date, datetime, time, timedelta
from odoo import SUPERUSER_ID
from odoo.http import request
from odoo.tools.translate import _
from odoo.http import Response
from odoo import http

_logger = logging.getLogger(__name__)


class Home(odoo.addons.web.controllers.main.Home):
	@http.route('/web/login', type='http', auth="none")
	def web_login(self, redirect=None, **kw):
		odoo.addons.web.controllers.main.ensure_db()
		request.params['login_success'] = False

		if request.httprequest.method == 'GET' and redirect and request.session.uid:
			return http.redirect_with_hash(redirect)

		if not request.uid:
			request.uid = odoo.SUPERUSER_ID

		values = request.params.copy()
		if not redirect:
			redirect = '/web?' + request.httprequest.query_string
		values['redirect'] = redirect

		try:
			values['databases'] = http.db_list()
		except odoo.exceptions.AccessDenied:
			values['databases'] = None

		if request.httprequest.method == 'POST':
			old_uid = request.uid
			uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
			if uid is not False:
				return http.redirect_with_hash(redirect)
			request.uid = old_uid
			values['error'] = "Login failed due to one of the following reasons"
			values['error2'] = "- Wrong login/password"
			values['error3'] = "- User already logged in from another system"
		return request.render('web.login', values)


class RootNew(odoo.http.Root):
	def get_response(self, httprequest, result, explicit_session):
		if isinstance(result, type(Response)) and result.is_qweb:
			try:
				result.flatten()
			except(Exception), e:
				if request.db:
					result = request.registry['ir.http']._handle_exception(e)
				else:
					raise

		if isinstance(result, basestring):
			response = Response(result, mimetype='text/html')
		else:
			response = result

		if httprequest.session.should_save:
			self.session_store.save(httprequest.session)
		# We must not set the cookie if the session id was specified using a http header or a GET parameter.
		# There are two reasons to this:
		# - When using one of those two means we consider that we are overriding the cookie, which means creating a new
		#   session on top of an already existing session and we don't want to create a mess with the 'normal' session
		#   (the one using the cookie). That is a special feature of the Session Javascript class.
		# - It could allow session fixation attacks.
		if not explicit_session and hasattr(response, 'set_cookie'):
			response.set_cookie('session_id', httprequest.session.sid, max_age=2 * 60)

		return response

root = RootNew()
odoo.http.Root.get_response = root.get_response


class ResUsers(models.Model):
	_inherit = 'res.users'

	session_id = fields.Char('Session ID', size=100)
	expiration_date = fields.Datetime('Expiration Date')
	logged_in =fields.Boolean('Logged in')

	@classmethod
	def _login(cls, db, login, password):
		user_id = super(ResUsers, cls)._login(db, login, password)

		try:
			with cls.pool.cursor() as cr:
				cr.autocommit(True)
				self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
				session_id = request.httprequest.session.sid
				temp_browse = self.browse(user_id)

				if isinstance(temp_browse, list): temp_browse = temp_browse[0]
				exp_date = temp_browse.expiration_date
				if exp_date and temp_browse.session_id:
					exp_date = datetime.strptime(exp_date,"%Y-%m-%d %H:%M:%S")
					if exp_date < datetime.utcnow() or temp_browse.session_id != session_id:
						raise odoo.exceptions.AccessDenied()
				self.save_session(user_id)
		except odoo.exceptions.AccessDenied:
			user_id = False
			_logger.warn("User %s is already logged in into the system!", login)
			_logger.warn("Multiple sessions are not allowed for security reasons!")

		return user_id


	@api.model
	def clear_session(self, user_id):
		"""clears session_id and session expiry from res.users"""
		if isinstance(user_id, list): user_id = user_id[0]
		user_obj = self.search([('id', '=', user_id)])
		user_obj.write({'session_id':'','expiration_date':False,'logged_in':False})

	@api.model
	def save_session(self, user_id):
		"""insert session_id and session expiry into res.users"""
		if isinstance(user_id, list): user_id = user_id[0]
		exp_date = datetime.utcnow() + timedelta(minutes=2)
		sid = request.httprequest.session.sid
		user_obj = self.search([('id', '=', user_id)])
		user_obj.write({'session_id':sid,'expiration_date':exp_date,'logged_in':True})

	@api.model
	def validate_sessions(self):
		"""schedular function to validate users session"""
		_ids = self.search([('expiration_date','!=',False)]).ids
		users = self.browse(_ids)

		for user_id in users:
			exp_date = datetime.strptime(user_id.expiration_date,"%Y-%m-%d %H:%M:%S")
			if exp_date < datetime.utcnow():
				self.clear_session(user_id.id)
