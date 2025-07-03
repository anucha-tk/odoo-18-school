{
    "name": "Todo App",
    "version": "1.0",
    "depends": ["base", "web"],
    "data": [
        "views/dashboard_view.xml",
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
