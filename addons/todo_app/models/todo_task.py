# addons/todo_app/models/todo_task.py
from odoo import fields, models


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo Task"

    name = fields.Char("Description", required=True)
    is_done = fields.Boolean("Done?", default=False)
    date_deadline = fields.Date("Deadline")
    user_id = fields.Many2one(
        "res.users", string="Responsible", default=lambda self: self.env.user
    )
    tag_ids = fields.Many2many("todo.task.tag", string="Tags")

    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    def do_clear_done(self):
        done_tasks = self.search([("is_done", "=", True)])
        done_tasks.unlink()
        return True


class TodoTaskTag(models.Model):
    _name = "todo.task.tag"
    _description = "Todo Task Tag"

    name = fields.Char("Tag Name", required=True)
