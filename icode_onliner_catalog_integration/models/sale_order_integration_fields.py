from odoo import fields, models, api

STATUSES = [
    ('new', 'new'),
    ('processing', 'processing'),
    ('confirmed', 'confirmed'),
    ('shipping', 'shipping'),
    ('delivered', 'delivered'),
    ('shop_canceled', 'shop canceled')
]

PAYMENT_TYPES = [
    ('1', 'cash'),
    ('2', 'terminal'),
    ('3', 'cashless')
]


class SaleOrderIntegrationFields(models.Model):
    _inherit = 'sale.order'

    key = fields.Char('Onliner Order Key')
    onliner_delivery_state = fields.Selection(STATUSES)
    updated_at = fields.Datetime('Last update date')
    # prices_definition = fields.Monetary()
