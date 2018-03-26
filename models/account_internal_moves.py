# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInternalMoves(models.Model):
	_inherit = "account.payment"


	vap_type = fields.Selection([
		('draft', 'Otros'), 
		('c2b', 'Caja a Bancos'),
		('b2c', 'Bancos a Caja')], 
		required=True, default='draft', copy=False, string="Tipo de transferencia")


	concept_related = fields.Char(related="communication")
	

	@api.onchange('vap_type')
	def _accounts_needed(self):
		source_type = ""
		destination_type = ""
		if self.vap_type == 'b2c':
			source_type = "bank"
			destination_type = "cash"
		elif self.vap_type == 'c2b':
			source_type = "cash"
			destination_type = "bank"

		if self.vap_type != 'draft':
			origin_id = self.env['account.journal'].search(['&', ('journal_user', '=', True), ('type', '=', source_type), ('company_id','=',self.company_id)])
			destination_id = self.env['account.journal'].search(['&', ('journal_user', '=', True), ('type', '=', destination_type), ('company_id','=',self.company_id)])
			self.journal_id = origin_id.id
			self.destination_id = destination_id.id