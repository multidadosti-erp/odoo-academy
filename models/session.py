# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import ValidationError


class Session(models.Model):

    _name = 'odoo.academy.session'

    name = fields.Char(string="Nome", required=True)
    start_data = fields.Date(string="Data inicio")
    duration = fields.Integer(string="Duração")
    seats = fields.Integer(string="Cadeiras")
    tel = fields.Char()
    email = fields.Char()
    local_street = fields.Char()

    instructor_id = fields.Many2one(comodel_name="res.partner",
                                    string="Instrutor",
                                    domain=['&', ('is_student', '=', False),('title.name', 'like', 'Doutor')])

    students_ids = fields.One2many(comodel_name="res.partner",
                                   inverse_name="session_id",
                                   string="Estudantes")

    occupied_seats = fields.Integer(string="Cadeiras Restantes", compute='_occupied_seats')

    @api.depends('seats', 'students_ids')
    def _occupied_seats(self):
        for s in self:
            s.occupied_seats = s.seats - len(s.students_ids)

    @api.onchange('instructor_id')
    def _update_end(self):
        for s in self:
            if s.instructor_id:
                s.local_street = s.instructor_id.street

    @api.constrains('students_ids')
    def _check_seats(self):
        for record in self:
            if record.occupied_seats < 0:
                raise ValidationError("Não há mais cadeiras disponíveis!")

    @api.one
    def search_attr_instructor(self):
        if self.instructor_id:
            self.write({'tel': self.instructor_id.phone, 'email': self.instructor_id.email})