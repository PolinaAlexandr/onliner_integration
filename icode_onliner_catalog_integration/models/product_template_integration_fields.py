from odoo import fields, models, api


class ProductTemplateIntegrationFields(models.Model):
    _inherit = 'product.template'

    importer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade')
    producer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade')
    vendor = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade')
    is_cashless = fields.Boolean(string='Is Cashless')
    is_credit = fields.Boolean(string='Is Credit')
    service_centers = fields.Char(string='Service Centers')
    delivery_country_id = fields.Many2one('res.country', string='Country',
                                          default=lambda self: self.env.ref('base.by').id)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.ref('base.by').id.currency_id)
    delivery_town_time = fields.Date()
    delivery_town_price = fields.Monetary(currency_field='currency_id')
    delivery_country_time = fields.Date()
    delivery_country_price = fields.Monetary(currency_field='currency_id', )
    warranty = fields.Selection([('1', 'No Warranty'), ('2', '1 Year'), ('3', '2 Years')], string='Warranty',
                                default='2')
    # TODO добавить регионы доставки возможно в фомате м2м поля или же selection
    # courierDeliveryPrices = fields.Many2many('product.template', string='Regions')
