# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    employee_id = fields.Many2one("hr.employee", string="Assigned Employee")
    manager_id = fields.Many2one("hr.employee", string="Manager")

    @api.model
    def get_values(self):
        """Retrieve values for fields in res.config.settings."""
        res = super(ResConfigSettings, self).get_values()
        IrConfigParam = self.env["ir.config_parameter"].sudo()

        # Retrieve the values from the ir.config_parameter model
        employee_id = (
            int(IrConfigParam.get_param("res.config.settings.employee_id"))
            if IrConfigParam.get_param("res.config.settings.employee_id")
            else False
        )
        manager_id = (
            int(IrConfigParam.get_param("res.config.settings.manager_id"))
            if IrConfigParam.get_param("res.config.settings.manager_id")
            else False
        )

        # Update the res dictionary with the retrieved values
        res.update(employee_id=employee_id, manager_id=manager_id)
        return res

    def set_values(self):
        """Save values from res.config.settings into ir.config_parameter."""
        super(ResConfigSettings, self).set_values()
        IrConfigParam = self.env["ir.config_parameter"].sudo()

        # Save the values into the ir.config_parameter model
        IrConfigParam.set_param(
            "res.config.settings.employee_id", self.employee_id.id
        )
        IrConfigParam.set_param(
            "res.config.settings.manager_id", self.manager_id.id
        )
