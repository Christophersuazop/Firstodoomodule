# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'this is an Addon'

    payment_mode = fields.Selection(
        string = "Payment mode",
        selection=[
            ('cash', "Cash"),
            ('bank', "Bank"),
            ('electronic', "Electronic")
        ]
    )