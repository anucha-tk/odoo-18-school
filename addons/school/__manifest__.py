{
    "name": "School",
    "version": "1.0",
    "description": "school management system for odoo",
    "summary": "school management system",
    "sequence": -100,
    "author": "anucha",
    "website": "",
    "license": "LGPL-3",
    "category": "",
    "depends": [
        "mail",
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/teacher_view.xml",
        # "views/student_view.xml",
    ],
    "demo": [""],
    "auto_install": False,
    "application": False,
    "assets": {},
}
