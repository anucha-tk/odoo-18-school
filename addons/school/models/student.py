from odoo import fields, models


class Student(models.Model):
    _name = "school.student"
    _description = "Student"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
