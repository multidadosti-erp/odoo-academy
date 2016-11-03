# -*- coding: utf-8 -*-

from openerp import fields, models

class Partner(models.Model):

    _inherit = 'res.partner'

    session_id = fields.Many2one(comodel_name="odoo.academy.session",
                                 string="Session")

    is_student = fields.Boolean("Estudante", default=True)
