from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    # product_category = fields.Char()
    # vendor = fields.Char()
    # model = fields.Char()
    # price = fields.Monetary()
    # currency = fields.Many2one('')
    # comment = fields.Char()
    # producer = fields.Char()
    # importer = fields.Char()
    # serviceCenters = fields.Char()
    # warranty = fields.Char()
    # deliveryTownTime = fields.Char()
    # deliveryTownPrice = fields.Monetary()
    # deliveryCountryTime = fields.Char()
    # deliveryCountryPrice = fields.Monetary()
    # productLifeTime = fields.Char()
    # isCashless = fields.Boolean()
    # isCredit = fields.Boolean()
    # stockStatus = fields.Char()
    # courierDeliveryPrices = fields.Selection()
    product_ids = fields.Many2many('product.template', string='Selected Products')
    names = fields.Char(string='Names')
    product_count = fields.Integer()
    importer = fields.Many2one()
    currency = fields.Many2one()

    # @api.onchange('product_ids')
    # def _compute_product_ids(self):
    #     product_data = self.env['product.template'].read_group(
    #         [('active_ids', 'in', self.ids)],
    #         ['active_ids'], ['active_ids'])
    #
    #     mapped_data = {datum['active_ids'][0]: datum['product_count'] for datum in product_data}
    #
    #     for product in self:
    #         product.product_count = mapped_data.get(product.id, 0)

    def send_data(self):
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        # for product in products:
        #     product_id = product.id
        #     category = product.categ_id.name
        #     vendor = product.producer.name
        #     importer = product.importer.name
        #     model = product.name
        #     price = product.list_price
        #     currency = product.currency_id.name
        #     producer = product.producer.name
        #     comment = product.extra_description
        #     service_centers = product.service_centers
        #     warranty = product._fields['warranty'].selection  # list
        #     delivery_town_time = product.delivery_town_time
        #     delivery_town_price = product.delivery_town_price
        #     delivery_country_time = product.delivery_country_time
        #     delivery_country_price = product.delivery_country_price
        #     product_life_time = product.exploitation_period
        #     is_cashless = product.is_cashless
        #     is_credit = product.is_credit

            # importer =

            # product_info = {
            #     "id": product_id,
            #     "category": category,
            #     "vendor": vendor,
            #     "model": model,
            #     "price": price,
            #     "currency": 'BYN',
            #     "comment": comment,
            #     "producer": producer,
            #     "importer": importer,
            #     "serviceCenters": service_centers,
            #     "warranty": [i for i in warranty if i[0] == product.warranty][0][1],
            #     "deliveryTownTime": delivery_town_time,
            #     "deliveryTownPrice": delivery_town_price,
            #     "deliveryCountryTime": delivery_country_time,
            #     "deliveryCountryPrice": delivery_country_price,
            #     "productLifeTime": product_life_time,
            #     "isCashless": is_cashless,
            #     "isCredit": is_credit,
            #     "stockStatus": "in_stock",
            #     "courierDeliveryPrices": {
            #         "region-1": {
            #             "type": "custom",
            #             "amount": "2.99"
            #         },
            #         "region-2": {
            #             "type": "no"
            #         }
            #     }
            # }

