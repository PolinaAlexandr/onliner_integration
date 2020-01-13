from odoo import fields , models, api


class IntegrationFields(models.Model):
    _inherit = 'product.template'

    producer_name = fields.Many2one('res.company', 'Company')
    is_cashless = fields.Boolean(string='Is Cashless?')
    is_credit = fields.Boolean(string='Is Credit?')
    service_centers = fields.Char(string='Service Centers')
    delivery_town_time = fields.date()
    delivery_town_price = fields.Monetary()
    delivery_country_time = fields.date()
    delivery_country_price = fields.date()

    delivery_country_id = fields.Many2one('res.country', 'Country',
                                          default=lambda self: self.env['res.country'].search(['code', '=', 'BY']))
    # courierDeliveryPrices = fields.Many2many('product.template', 'product.template.', )
