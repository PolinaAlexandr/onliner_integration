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
    warranty = fields.Selection([('1', 'No Warranty'), ('2', '12 months'), ('3', '24 month')], string='Warranty',
                                default='2')
    # regions = fields.Selection([('1', 'Minsk region'), ('2', 'Grodno region'), ('3', 'Vitebsk region'),
    #                             ('4', 'Mogilev region'), ('5', 'Brest region'), ('6', "Gomel' region")],
    #                            string='Delivery Regions')
    terms_of_delivery = fields.Selection([('1', 'default'), ('2', 'none'), ('3', 'custom')])
    # custom_term = fields.Monetary(currency_field='currency_id', domain=[('terms_of_delivery', '=', 'custom')])
    # TODO добавить регионы доставки возможно в фомате м2м поля или же selection
    # courier_delivery_prices = fields.Many2many('res.country.state', 'regions_ids', string='Regions')
    # region1 = fields.Boolean(string='Minsk region')
    # region2 = fields.Boolean(string='Grodno region')
    # region3 = fields.Boolean(string='Vitebsk region')
    # region4 = fields.Boolean(string='Mogilev region')
    # region5 = fields.Boolean(string='Brest region')
    # region6 = fields.Boolean(string="Gomel' region")
