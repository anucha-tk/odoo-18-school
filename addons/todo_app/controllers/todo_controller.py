from odoo import http
from odoo.http import request


class TodoController(http.Controller):
    @http.route("/todos", type="http", auth="public", website=True)
    def todo_listing_page(self, **kwargs):
        return request.render("partner_website_listing.partner_listing_page")

    @http.route("/todo/data", type="json", auth="public", website=True)
    def get_todos(self):
        todos_data = (
            request.env["todo.task"]
            .sudo()
            .search_read(
                domain=[],  # An empty domain means fetch all todo.task records
                # Specify all the fields your QWeb template expects:
                fields=[
                    "id",
                    "name",
                    "is_done",
                    "date_deadline",
                    "user_id",
                    "tag_ids",
                ],
                order="date_deadline asc, name asc",  # Example: order by deadline then name
                limit=100,  # Example: limit the number of records
            )
        )

        # The result of search_read() is already a list of dictionaries,
        # so you can directly return it under the key expected by your JavaScript (result.todo).
        return {
            "todo": todos_data,  # <--- Changed key to "todo" for consistency with your JS
            "message": "Todo data fetched successfully!",  # Optional: add a success message
        }
