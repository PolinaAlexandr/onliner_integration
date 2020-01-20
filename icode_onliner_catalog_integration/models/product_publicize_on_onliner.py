import json
import requests
import random

from odoo import fields, models, api


class OnlinerCatalog(models.Model):
    _inherit = 'product.template'

    # TODO открывать поля чьи значения не заданы/имеют не подходящие данные на форме визарда и при вводе напрямую записывать значения в словарь

    def publicize_on_onliner(self):
        form_id = self.env.ref('icode_onliner_catalog_integration.product_template_get_product_info_wizard_view').id
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        product_info = {}
        data = []
        # nums = random.randint(0, 1000)
        for product in products:
            product_id = product.id
            category = product.categ_id.name
            vendor = product.producer.name
            importer = product.importer.name
            model = product.name
            price = product.list_price
            currency = product.currency_id.name
            producer = product.producer.name
            comment = product.extra_description
            service_centers = product.service_centers
            warranty = product._fields['warranty'].selection #list
            delivery_town_time = product.delivery_town_time
            delivery_town_price = product.delivery_town_price
            delivery_country_time = product.delivery_country_time
            delivery_country_price = product.delivery_country_price
            product_life_time = product.exploitation_period
            is_cashless = product.is_cashless
            is_credit = product.is_credit

            # for i in product.mapped(i) == [] or () or False or 0 :

            product_info = {
                "id": product_id,
                "category": category,
                "vendor": vendor,
                "model": model,
                "price": price,
                "currency": 'BYN',
                "comment": comment,
                "producer": producer,
                "importer": importer,
                "serviceCenters": service_centers,
                "warranty": [i for i in warranty if i[0] == product.warranty][0][1],
                "deliveryTownTime": delivery_town_time,
                "deliveryTownPrice": delivery_town_price,
                "deliveryCountryTime": delivery_country_time,
                "deliveryCountryPrice": delivery_country_price,
                "productLifeTime": product_life_time,
                "isCashless": is_cashless,
                "isCredit": is_credit,
                "stockStatus": "in_stock",
                "courierDeliveryPrices": {
                    "region-1": {
                        "type": "custom",
                        "amount": "2.99"
                    },
                    "region-2": {
                        "type": "no"
                    }
                }
            }

            data.append(product_info)

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'product.template.get_product_info_wizard',
                'view_mode': 'form',
                'views': [(form_id, 'form')],
                'context': {
                    'default_product_ids': active_ids,
                    'default_names': product_info,
                    # 'default_importer': importer,
                    # 'default_currency': currency,
                    # 'default_product_life_time': product_life_time,
                    # 'default_product_count': product_count,
                },
                'target': 'new'}



    # def form_request(self, data, params):
    #         url = "https://b2bapi.onliner.by/pricelists"
    #         token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
    #         header = {
    #             'Accept': 'application/json',
    #             'Content-Type': 'application/json',
    #             'Authorization': token}
    #         request = requests.put(url, data, headers=header)
