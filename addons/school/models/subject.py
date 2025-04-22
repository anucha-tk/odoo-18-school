from odoo import fields, models


class Subject(models.Model):
    _name = "school.subject"
    _description = "School Subject"
    _rec_name = "name"

    name = fields.Char(string="Subject Name", required=True)
    code = fields.Char(string="Subject Code", required=True)
    description = fields.Text(string="Description")
    teacher_id = fields.Many2one(
        "school.teacher", string="Teacher", required=True
    )
    student_ids = fields.Many2many("school.student", string="Students")
    status_id = fields.Many2one("school.subject.status", string="Status")


class SubjectStatus(models.Model):
    _name = "school.subject.status"
    _description = "School Subject Status"
    _order = "sequence"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence", default="10")
