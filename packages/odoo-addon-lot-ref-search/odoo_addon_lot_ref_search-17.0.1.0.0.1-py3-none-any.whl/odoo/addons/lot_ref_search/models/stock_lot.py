# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class StockLot(models.Model):
    _inherit = "stock.lot"

    _rec_names_search = ["name", "ref"]

    @api.depends("name")
    def _compute_display_name(self):
        for rec in self:
            ref_text = f"[{rec.ref}] " if rec.ref else ""
            rec.display_name = f"{ref_text}{rec.name}"
