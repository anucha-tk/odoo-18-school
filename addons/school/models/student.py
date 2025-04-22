from odoo import fields, models


class Student(models.Model):
    _name = "school.student"
    _description = "Student"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    teacher_id = fields.Many2one("school.teacher", string="Teacher")
    gender = fields.Selection(
        [
            ("Male", "male"),
            ("Female", "female"),
        ],
        string="gender",
        required=True,
    )
    status = fields.Selection(
        [
            ("active", "Active"),
            ("in_active", "In Active"),
            ("reject", "Reject"),
        ],
        string="status",
        default="active",
        required=True,
    )
