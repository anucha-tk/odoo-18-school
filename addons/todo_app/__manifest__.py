{
    "name": "Todo App",
    "version": "1.0",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/dashboard_view.xml",
        "views/todo_task_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "todo_app/static/src/**",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
