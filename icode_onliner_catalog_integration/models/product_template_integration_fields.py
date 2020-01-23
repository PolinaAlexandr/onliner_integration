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
    delivery_type = fields.Selection(DELIVERY_TYPE)
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')])
    price = fields.Monetary(currency_field=currency_id, default=0)


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
    delivery_town_time = fields.Date()
    delivery_town_price = fields.Monetary(currency_field='currency_id')
    delivery_country_time = fields.Date()
    delivery_country_price = fields.Monetary(currency_field='currency_id', )
    warranty = fields.Selection([('1', 'No Warranty'), ('2', '12 months'), ('3', '24 month')], string='Warranty',
                                default='2')
    courier_delivery_price = fields.One2many('product.template.onliner.line', 'product_id')


class ResCountryStateInverseIntegrationFields(models.Model):
    _name = 'product.template.onliner.line'

    product_id = fields.Many2one('product.template')

    # def set_params(self):
    #     name = self.env['delivery_country_data'].sudo().get_param('product_template_onliner_line.name', default='')
    #     code = self.env['ir.config_parameter'].sudo().get_param('product_template_onliner_line.code', default='')
    #     type = self.env['ir.config_parameter'].sudo().get_param('product_template_onliner_line.type', default='')
    #     currency_id = self.env['ir.config_parameter'].sudo().get_param('product_template_onliner_line.currency_id', default='')
    #     amount = self.env['ir.config_parameter'].sudo().get_param('product_template_onliner_line.amount', default='')
    #
    #     return name, code, type, currency_id, amount

    # TODO иметь возможность выбрать регионы относящиеся исключительно к РБ
    #  (варинат м20 лишает возможности выбора нескольких регионов)
    # TODO для каждого из указанных регионов предоставить варианты стоимости доставки
    #  (type: custom, free, default, no )
    # TODO type:custom : при выборе данного типа должно открываться окно для ввода цены "amount(Monetary)"
    # TODO type:free : простая запись значения
    # TODO type:default :
    #  величина определяется со стороны онлайнера и имеет денежный эквивалент только на их ресурсе
    # TODO type:no :
    #  (вероятнее всего служит индикатором наличия региона в тарифной сети)
    # TODO Вопросы к решению:
    #  1) тип поля отвечающего за регионы доставки: необходима опция выбора от одного до шести(изначально) регионов
    #  (возможность насширения региональнойй сети)(res.config.settings)
    #  2) Цены доставки в рамках областных центрах
    # TODO post_init функция, create/write для продуктов, запретить редактирования в security


