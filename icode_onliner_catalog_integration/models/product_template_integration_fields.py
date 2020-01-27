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

    importer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    producer = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    vendor = fields.Many2one('res.company',  default=lambda self: self.env.company, ondelete='cascade', required=True)
    is_cashless = fields.Boolean(string='Is Cashless')
    is_credit = fields.Boolean(string='Is Credit')
    service_centers = fields.Char(string='Service Centers', default='Some Address Here',  required=True)
    delivery_country_id = fields.Many2one('res.country', string='Country',
                                          default=lambda self: self.env.ref('base.by').id, required=True)
    delivery_town_time = fields.Date()
    delivery_town_price = fields.Monetary(currency_field='currency_id')
    delivery_country_time = fields.Date()
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

    # @api.onchange('courier_delivery_price_ids')
    # def check_duplications(self):
    #     if self.courier_delivery_price_ids:
    #         existing_names = self.courier_delivery_price_ids.mapped('name')
    #         domain = [(self.name, 'not in', existing_names)]
    #         return {'domain': {'courier_delivery_price_ids': domain}}


class ProductOnlinerRegionSettingsLine(models.Model):
    _name = 'product.onliner.region_settings.line'

    name = fields.Selection(REGIONS, required=True, readonly=True)
    product_id = fields.Many2one('product.template', string='Courier Delivery Price')
    delivery_type = fields.Selection(DELIVERY_TYPE, required=True)
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')],
                                  default=lambda self: self.env.ref('base.BYN', required=True))
    price = fields.Monetary(currency_field='currency_id', reuired=True)

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
    # TODO post_init функция(заменяет overriding методов create/write, автоматически
    #  выставляя значения во все существующие продукты по установке модуля),
    #  create/write для продуктов, урезать доступ в security
