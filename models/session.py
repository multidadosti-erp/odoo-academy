# -*- coding: utf-8 -*-

from openerp import fields, models


class Session(models.Model):

    _name = 'odoo.academy.session'

    name = fields.Char(string="Nome", required=True)
    start_data = fields.Date(string="Data inicio")
    duration = fields.Integer(string="Duração")
    seats = fields.Integer(string="Cadeiras")
<<<<<<< 0d99a3db3c0865d5a53aab0b1e7c679eab570cfc
    course_id = fields.Many2one(comodel_name="odoo.academy.courses",
                                 string="Courses")
=======
>>>>>>> [FIX] many2many courses

    instructor_id = fields.Many2one(comodel_name="res.partner",
                                    string="Instrutor")

    students_ids = fields.One2many(comodel_name="res.partner",
                                   inverse_name="session_id",
                                   string="Estudantes")


class ResPartner(models.Model):

    _inherit = 'res.partner'

    session_id = fields.Many2one(comodel_name="odoo.academy.session",
                                 string="Session")

