# -*- coding: utf-8 -*-

from ast import literal_eval
from odoo import models


class HREmployee(models.Model):
    _inherit = "hr.employee"

    def _compute_display_name(self):
        """Method to compute display name"""
        for rec in self:
            if (
                "params" in self._context
                and "model" in self._context.get("params")
                and "is_manager" not in self._context
                and self._context.get("params").get("model")
                == "res.config.settings"
            ):
                rec.display_name = f"{rec.name}"
            else:
                rec.display_name = f"{rec.name} - {rec.work_email}"

    def action_open_timesheet(self):
        """Open the timesheet view for the current employee."""
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "hr_timesheet.timesheet_action_from_employee"
        )
        context = literal_eval(
            action["context"].replace("active_id", str(self.id))
        )
        context["create"] = context.get("create", True) and self.active
        context["grid_range"] = "week"
        action["context"] = context
        return action
