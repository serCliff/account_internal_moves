# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AccountInternalMoves(models.Model):
	_inherit = "account.payment"


	vap_type = fields.Selection([
		('draft', 'Otros'), 
		('c2b', 'Caja a Bancos'),
		('b2c', 'Bancos a Caja')], 
		required=True, default='draft', copy=False, string="Tipo de transferencia")

	transfer_time = fields.Datetime(string='Hora de transferencia', default=fields.Datetime.now, readonly=True)
	concept_related = fields.Char(related="communication")
	

	@api.onchange('vap_type')
	def _accounts_needed(self):
		"""
			FILLS THE ACCOUNT JOURNALS TO FIT WITH SELECTED vap_type OPPERATION
		"""
		source_type = ""
		destination_type = ""

		if self.vap_type == 'b2c':
			source_type = "bank"
			destination_type = "cash"
		elif self.vap_type == 'c2b':
			source_type = "cash"
			destination_type = "bank"

		if self.vap_type != 'draft':
			origin_id = self.env['account.journal'].search(['&', ('journal_user', '=', True), ('type', '=', source_type), ('company_id','=',self.env.user.company_id.id)])
			destination_id = self.env['account.journal'].search(['&', ('journal_user', '=', True), ('type', '=', destination_type), ('company_id','=',self.env.user.company_id.id)])
			self.journal_id = origin_id.id
			self.destination_journal_id = destination_id.id
		else:
			self.journal_id = False
			self.destination_journal_id = False


class PosConfigMethod(models.Model):

	_inherit = "pos.config"


	@api.multi
	def action_internal_transfer(self):
		assert len(self.ids) == 1, "you can open only one session at a time"

		return {
		    'name': _('Transferencia Interna'),
		    'view_type': 'form',
		    'view_mode': 'form,tree',
		    'res_model': 'account.payment',
		    'context': {'default_payment_type': 'transfer', 'default_vap_type': 'c2b', 'default_partner_type': ''},
		    'domain': [('payment_type', '=', 'transfer')],
		    'view_id': False,
		    'type': 'ir.actions.act_window',
		}







