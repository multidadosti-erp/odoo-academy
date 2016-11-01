# -*- coding: utf-8 -*-

from openerp import fields, models


class Courses(models.Model):

    _name = 'odoo.academy.courses'

    name = fields.Char(string="Nome", required=True)

    sessions_ids = fields.One2many(comodel_name="odoo.academy.session",
                                   inverse_name="course_id",
                                   string="Cursos")