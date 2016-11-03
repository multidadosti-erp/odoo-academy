# -*- coding: utf-8 -*-

from openerp import fields, models


class Courses(models.Model):

    _name = 'odoo.academy.courses'

    name = fields.Char(string="Nome", required=True)

    sessions_ids = fields.Many2many('odoo.academy.session', string="Aulas")

