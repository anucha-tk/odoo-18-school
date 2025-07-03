{
    "name": "Todo App",
    "version": "1.0",
    "depends": ["base", "web"],
    "data": [
        # Remove this line: "views/web_asset_backend_template.xml",
        # Add other necessary XML files here, if any (e.g., security, regular views)
    ],
    "assets": {
        "web.assets_backend": [
            "/todo_app/static/src/js/dashboard.js",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
