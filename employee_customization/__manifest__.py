# -*- coding: utf-8 -*-

{
    "name": "Employee Customization",
    "version": "17.0.1.0.1",
    "category": "hr",
    "summary": "Employee Customization",
    "description": """
        Employee Customization
        ======================================
        This module manage the employee dropdown, Employee Timesheet with new 
        quarterly filter.
    """,
    "author": "Aktiv Software",
    "company": "Aktiv Software",
    "website": "https://www.aktivsoftware.com",
    "depends": ["hr_timesheet"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/hr_employee_views.xml",
        "views/account_analytic_line_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "LGPL-3",
}
