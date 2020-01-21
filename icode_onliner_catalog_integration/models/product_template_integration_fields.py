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
    delivery_town_time = fields.Date()
    delivery_town_price = fields.Monetary(currency_field='currency_id')
    delivery_country_time = fields.Date()
    delivery_country_price = fields.Monetary(currency_field='currency_id', )
    warranty = fields.Selection([('1', 'No Warranty'), ('2', '12 months'), ('3', '24 month')], string='Warranty',
                                default='2')
    courier_delivery_prices = fields.One2many('product.template.onliner.line', 'product_id')


class ResCountryStateInverseIntegrationFields(models.Model):
    _name = 'product.template.onliner.line'

    product_id = fields.Many2one('product.template')
    country_id = fields.Many2one('res.country', string='Country', default=lambda self: self.env.ref('base.by').id)
    region = fields.Many2one('res.country.state', domain=[('country_id.name', '=', 'Belarus')])

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


    # Создать data файл для регионов доставки и изначально указать значение default,
    # пользователь сможет менять значения самостоятельно однако при отсуствии ааеденных значений всегда вернется default
    # так же значения в data файлах неизменяемы пользователями(в базе)
    # code = fields.Char(related='states.name.code')



