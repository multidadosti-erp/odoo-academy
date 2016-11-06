# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import ValidationError
import time


class Session(models.Model):

    _name = 'odoo.academy.session'

    name = fields.Char(string="Nome", required=True)
    start_data = fields.Date(string="Data inicio", inverse="_set_data_session")
    duration = fields.Integer(string="Duração")
    seats = fields.Integer(string="Cadeiras")
    tel = fields.Char()
    email = fields.Char()
    company = fields.Char()
    course = fields.Char(string="Nome do Curso")
    l_title = fields.Many2one(related="instructor_id.title")
    period = fields.Selection([(u'manhã', 'Manhã'), (u'tarde', 'Tarde'), (u'noite', 'Noite')])


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
            s.company = self.env['res.partner'].search([('name', '=', self.instructor_id.name)]).parent_id.name

    @api.constrains('students_ids')
    def _check_seats(self):
        for record in self:
            if record.occupied_seats < 0:
                raise ValidationError("Não há mais cadeiras disponíveis!")

    @api.one
    def search_attr_instructor(self):
        if self.instructor_id:
            self.write({'tel': self.instructor_id.phone, 'email': self.instructor_id.email})

    @api.one
    def submit_new_course(self):
        if self.course:
            self.env['odoo.academy.courses'].create({'name': self.course})

    def _set_data_session(self):
        if not self.start_data:
            self.write({'start_data': fields.date.today()})