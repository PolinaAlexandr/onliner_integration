from odoo import fields, models, api


class ProductTemplateIntegrationFields(models.Model):
    _inherit = 'product.template'

    producer_name = fields.Many2one('res.company', 'Company')
    is_cashless = fields.Boolean(string='Is Cashless?')
    is_credit = fields.Boolean(string='Is Credit?')
    service_centers = fields.Char(string='Service Centers')
    currency_id = fields.Many2one('res.currency', string='Currency')
    delivery_town_time = fields.Date()
    delivery_town_price = fields.Monetary(currency_field='currency_id')
    delivery_country_time = fields.Date()
    delivery_country_price = fields.Monetary(currency_field='currency_id')
    delivery_country_id = fields.Many2one('res.country', string='Country',
                                          default=lambda self: self.env.ref('base.by').id)
    # courierDeliveryPrices = fields.Many2many('product.template'
