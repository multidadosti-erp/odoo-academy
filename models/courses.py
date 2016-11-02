# -*- coding: utf-8 -*-

from openerp import fields, models


class Courses(models.Model):

    _name = 'odoo.academy.courses'

    name = fields.Char(string="Nome", required=True)

<<<<<<< 0d99a3db3c0865d5a53aab0b1e7c679eab570cfc
    sessions_ids = fields.One2many(comodel_name="odoo.academy.session",
                                   inverse_name="course_id",
                                   string="Cursos")
=======
    sessions_ids = fields.Many2many('odoo.academy.session', string="Cursos")
>>>>>>> [FIX] many2many courses
