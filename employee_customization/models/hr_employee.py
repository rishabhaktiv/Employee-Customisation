# -*- coding: utf-8 -*-

from ast import literal_eval
from odoo import models


class HREmployee(models.Model):
    _inherit = "hr.employee"

    def _compute_display_name(self):
        """Method to compute display name"""
        for rec in self:
            # Check if "is_manager" is not in context
            is_manager = "is_manager" not in self._context
            # Get params from context
            params = self._context.get("params", {})
            model = params.get("model")
            module = self._context.get("module")
            # Define the conditions for display name computation
            if (
                    (model == "res.config.settings" or module in [
                        'general_settings', 'hr']) and
                    is_manager
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
