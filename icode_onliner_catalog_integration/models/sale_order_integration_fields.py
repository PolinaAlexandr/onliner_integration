from odoo import fields, models, api

STATUSES = [
    ('1', 'new'),
    ('2', 'processing'),
    ('3', 'confirmed'),
    ('4', 'shipping')
]

PAYMENT_TYPES = [
    ('1', 'cash'),
    ('2', 'terminal'),
    ('3', 'cashless')
]


class SaleOrderIntegrationFields(models.Model):
    _inherit = 'sale.order'

    key = fields.Char('Onliner Order Key')
    onliner_delivery_status = fields.Selection(STATUSES)
    updated_at = fields.Datetime('Last update date')
