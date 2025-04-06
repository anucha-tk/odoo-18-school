from odoo import fields, models


class School(models.Model):
    _name = "school"
    _description = "School"
    _rec_name = "name"
    _inherit = "mail.thread"

    name = fields.Char(string="School Name", required=True, tracking=True)
    address = fields.Text(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
