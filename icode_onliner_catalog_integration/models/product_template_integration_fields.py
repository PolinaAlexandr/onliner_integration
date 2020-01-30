from odoo import fields, models, api

REGIONS = [
    ('brest_region', 'Brest Region'),
    ('vitebsk_region', 'Vitebsk Region'),
    ('gomel_region', 'Gomel Region'),
    ('gordno_region', 'Gordno Region'),
    ('mogilev_region', 'Mogilev Region'),
    ('minsk_region', 'Minsk Region')
]


DELIVERY_TYPE = [
    ('no', 'no'),
    ('default', 'default'),
    ('custom', 'custom'),
    ('free', 'free')
]


class OnlinerRegionSettings(models.Model):
    _name = 'onliner.region_settings'

    name = fields.Selection(REGIONS)
    delivery_type = fields.Selection(DELIVERY_TYPE, required=True)
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')],
                                  default=lambda self: self.env.ref('base.BYN'))
    price = fields.Monetary(currency_field='currency_id', reuired=True)


class ProductTemplateIntegrationFields(models.Model):
    _inherit = 'product.template'

    exploitation_period = fields.Char(required=True, default='5 years')
    extra_description = fields.Html(default="Text Description")
    importer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    producer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    vendor = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    is_cashless = fields.Boolean(string='Is Cashless') # Флаг предложения для юридических лиц (1 - для юридических, 0 - для физических)
    is_credit = fields.Boolean(string='Is Credit') # Флаг доступности покупки в кредит (1 - можно, 0 - нет)
    service_centers = fields.Char(string='Service Centers', default='Some Address Here',  required=True)
    delivery_country_id = fields.Many2one('res.country', string='Country', domain=[('name', '=', 'Belarus')],
                                          default=lambda self: self.env.ref('base.by').id, required=True)
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')], default=lambda self: self.env.ref('base.BYN'),
                                  readonly=False)
    delivery_town_time = fields.Selection([('1', 'One day'), ('2', 'Two days'), ('3', 'Three days')],
                                          string='Delivery Town Time', default='1', required=True)

    delivery_town_price = fields.Monetary(currency_field='currency_id')

    delivery_country_time = fields.Selection([('1', 'One day'), ('2', 'Two days'), ('3', 'Three days'), ('4', 'One week')],
                                             string='Delivery Country Time', default='2', required=True)

    delivery_country_price = fields.Monetary(currency_field='currency_id',)
    warranty = fields.Selection([('1', 'No Warranty'), ('2', '12 months'), ('3', '24 month')], string='Warranty',
                                default='2', required=True)

    courier_delivery_price_ids = fields.One2many('product.onliner.region_settings.line', 'product_id')

    @api.model
    def default_get(self, fields_list):
        res = super(ProductTemplateIntegrationFields, self).default_get(fields_list)
        delivery_vals = self.env['onliner.region_settings'].search([])
        result = []
        if delivery_vals:
            for delivery_val in delivery_vals:
                result.append((0, 0, {
                    'name': delivery_val.name,
                    'delivery_type': delivery_val.delivery_type,
                    'price': delivery_val.price,
                }))
        res.update({'courier_delivery_price_ids': result})
        return res


class ProductOnlinerRegionSettingsLine(models.Model):
    _name = 'product.onliner.region_settings.line'

    name = fields.Selection(REGIONS, required=True, readonly=True)
    product_id = fields.Many2one('product.template', string='Courier Delivery Price')
    delivery_type = fields.Selection(DELIVERY_TYPE, required=True)
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')],
                                  default=lambda self: self.env.ref('base.BYN'), required=True)
    price = fields.Monetary(currency_field='currency_id', reuired=True)
