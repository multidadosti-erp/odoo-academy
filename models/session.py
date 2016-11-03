# -*- coding: utf-8 -*-

from openerp import fields, models


class Session(models.Model):

    _name = 'odoo.academy.session'

    name = fields.Char(string="Nome", required=True)
    start_data = fields.Date(string="Data inicio")
    duration = fields.Integer(string="Duração")
    seats = fields.Integer(string="Cadeiras")

    instructor_id = fields.Many2one(comodel_name="res.partner",
                                    string="Instrutor")

    students_ids = fields.One2many(comodel_name="res.partner",
                                   inverse_name="session_id",
                                   string="Estudantes")


class ResPartner(models.Model):

    _inherit = 'res.partner'

    session_id = fields.Many2one(comodel_name="odoo.academy.session",
                                 string="Session")

