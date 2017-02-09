# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
	_name = 'mapletransform.wizard'

	def _def_transform(self):
		return self.env['mapletransform.mapletransform'].browse(self._context.get('active_id'))

	transform_id = fields.Many2one('mapletransform.mapletransform', required=True, default=_def_transform)
	barrel_id    = fields.Many2one('maplereception.barrel')

#	def addTransform(self):
#		self.barrel_id
#		return {}
