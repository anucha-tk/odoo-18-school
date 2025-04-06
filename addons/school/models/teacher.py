from odoo import fields, models


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"
    _rec_name = "name"
    _inherit = "mail.thread"

    name = fields.Char(string="Teacher Name", required=True, tracking=True)
    age = fields.Integer(string="Age")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    student_ids = fields.One2many(
        "school.student", "teacher_id", string="Students"
    )
