import json
import requests
import random

from odoo import fields, models, api


class OnlinerCatalog(models.Model):
    _inherit = 'product.template'

    def publicize_on_onliner(self):
        form_id = self.env.ref('icode_onliner_catalog_integration.product_template_get_product_info_wizard_view').id
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        product_info = {}
        data = {}
        nums = random.randint(0, 1000)
        for product in products:
            product_id = product.id
            category = product.categ_id.name
            vendor = product.producer_name.id
            importer = product.customer_info_ids
            model = product.name
            price = product.mapped('list_price')
            currency = "BYN"
            comment = product.extra_description
            serviceCenters = product.service_centers
            # w = product.warranry
            warranty = product._fields['warranty'].selection #list
            # warranty1 = [i for i in warranty if i == w] #list comprehention
            # warranty12 = len(warranty)

            deliveryTownTime = product.delivery_town_time
            deliveryTownPrice = product.delivery_town_price
            deliveryCountryTime = product.delivery_country_time
            deliveryCountryPrice = product.delivery_country_price
            productLifeTime = product.exploitation_period
            isCashless = product.is_cashless
            isCredit = product.is_credit
            # if importer.mapped('customer_info_ids').id == []:

            product_info = {
                "id": product_id,
                "category": category,
                "vendor": vendor,
                "model": model,
                "price": price,
                "currency": currency,
                "comment": comment,
                "producer": "Foxconn,No.2,2nd Donghuan Road,10th Yousong Industrial District",
                # "importer": product.customer_info_ids.ids,
                "importer": product.mapped('customer_info_ids'),
                "serviceCenters": serviceCenters,
                "warranty1": [i for i in warranty if i[0] == product.warranty][0][1],
                "deliveryTownTime": deliveryTownTime,
                "deliveryTownPrice": deliveryTownPrice,
                "deliveryCountryTime": deliveryCountryTime,
                "deliveryCountryPrice": deliveryCountryPrice,
                "productLifeTime": productLifeTime,
                "isCashless": isCashless,
                "isCredit": isCredit,
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
            data.update(product_info)
            # TODO добавить цикл обработки словарей с данными в качестве ключей к объекту data в "родительском" словаре data
            # TODO обойти при этом проблему перезаписи значения с идентичным именем. Варивнт форматирования названия(вероятнее всего уникальный ID каждого продукта)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template.get_product_info_wizard',
            'view_mode': 'form',
            'views': [(form_id, 'form')],
            'context': {
                'default_product_ids': active_ids,
                'default_names': product_info,
                # 'default_product_count': product_count,
            },
            'target': 'new'}

    def form_request(self, data, params):
            url = "https://b2bapi.onliner.by/pricelists"
            token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
            header = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token}
            request = requests.put(url, data, headers=header)
