import json
import requests

from odoo import fields, models, api


class OnlinerCatalog(models.Model):
    _inherit = 'product.template'

    # def publicize_on_onliner(self):
    #     active_id = self._context.get('active_id')
    #     active_ids = self._context.get('active_ids', [active_id] if active_id else [])
    #     Product = self.env['product.template']
    #     product = Product.browse(active_id)
    #     products = Product.browse(active_ids)
    #     product_info = {}
    #     data = []
    #     for product in products:
    #         product_id = product.id
    #         category = product.categ_id.name
    #         vendor = product.producer.name
    #         importer = product.importer.name
    #         model = product.name
    #         price = product.list_price
    #         currency = product.currency_id.name
    #         producer = product.producer.name
    #         comment = product.extra_description
    #         service_centers = product.service_centers
    #         warranty = product._fields['warranty'].selection  # list
    #         delivery_town_time = product._fields['delivery_town_time'].selection
    #         delivery_town_price = product.delivery_town_price
    #         delivery_country_time = product._fields['delivery_country_time'].selection
    #         delivery_country_price = product.delivery_country_price
    #         product_life_time = product.exploitation_period
    #         is_cashless = product.is_cashless
    #         is_credit = product.is_credit
    #         courier_delivery_price = {
    #             "region-1": {
    #                 "type": product.courier_delivery_price_ids[0].delivery_type,
    #                 "price": product.courier_delivery_price_ids[0].price},
    #             "region-2": {
    #                 "type": product.courier_delivery_price_ids[1].delivery_type,
    #                 "price": product.courier_delivery_price_ids[1].price},
    #             "region-3": {
    #                 "type": product.courier_delivery_price_ids[2].delivery_type,
    #                 "price": product.courier_delivery_price_ids[2].price},
    #             "region-4": {
    #                 "type": product.courier_delivery_price_ids[3].delivery_type,
    #                 "price": product.courier_delivery_price_ids[3].price},
    #             "region-5": {
    #                 "type": product.courier_delivery_price_ids[4].delivery_type,
    #                 "price": product.courier_delivery_price_ids[4].price},
    #             "region-6": {
    #                 "type": product.courier_delivery_price_ids[5].delivery_type,
    #                 "price": product.courier_delivery_price_ids[5].price}}
    #
    #         product_info = [{
    #             "id": product_id,
    #             "category": category,
    #             "vendor": vendor,
    #             "model": model,
    #             "price": price,
    #             "currency": currency,
    #             "comment": comment,
    #             "producer": producer,
    #             "importer": importer,
    #             "serviceCenters": service_centers,
    #             "warranty": [i for i in warranty if i[0] == product.warranty][0][1],
    #             "deliveryTownTime": [i for i in delivery_town_time if i[0] == product.delivery_town_time][0][1],
    #             "deliveryTownPrice": delivery_town_price,
    #             "deliveryCountryTime": [i for i in delivery_country_time if i[0] == product.delivery_country_time][0][1],
    #             "deliveryCountryPrice": delivery_country_price,
    #             "productLifeTime": product_life_time,
    #             "isCashless": is_cashless,
    #             "isCredit": is_credit,
    #             "stockStatus": "in_stock",
    #             "courierDeliveryPrices": courier_delivery_price
    #         }]
    #
    #         data.append(product_info)
    #
    #     json_data = json.dumps(data)
    #     url = "https://b2bapi.onliner.by/pricelists"
    #     token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
    #     header = {
    #         'Accept': 'application/json',
    #         'Content-Type': 'application/json',
    #         'Authorization': token}
    #     request = requests.patch(url, data=json_data, headers=header) #использовать тип запроса put при загрузке нового прайслиста и заменой всех данных
    #     return request
    #     # response_summary = json.loads(request.content.decode('utf-8'))

    def publicize_on_onliner(self):
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        product_info = {}
        data = []
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
            delivery_town_time = product._fields['delivery_town_time'].selection
            delivery_town_price = product.delivery_town_price
            delivery_country_time = product._fields['delivery_country_time'].selection
            delivery_country_price = product.delivery_country_price
            product_life_time = product.exploitation_period
            is_cashless = product.is_cashless
            is_credit = product.is_credit
            courier_delivery_price = {
                "region-1": {
                    "type": product.courier_delivery_price_ids[0].delivery_type,
                    "price": product.courier_delivery_price_ids[0].price},
                "region-2": {
                    "type": product.courier_delivery_price_ids[1].delivery_type,
                    "price": product.courier_delivery_price_ids[1].price},
                "region-3": {
                    "type": product.courier_delivery_price_ids[2].delivery_type,
                    "price": product.courier_delivery_price_ids[2].price},
                "region-4": {
                    "type": product.courier_delivery_price_ids[3].delivery_type,
                    "price": product.courier_delivery_price_ids[3].price},
                "region-5": {
                    "type": product.courier_delivery_price_ids[4].delivery_type,
                    "price": product.courier_delivery_price_ids[4].price},
                "region-6": {
                    "type": product.courier_delivery_price_ids[5].delivery_type,
                    "price": product.courier_delivery_price_ids[5].price}}

            product_info = [{
                "id": product_id,
                "category": category,
                "vendor": vendor,
                "model": model,
                "price": price,
                "currency": currency,
                "comment": comment,
                "producer": producer,
                "importer": importer,
                "serviceCenters": service_centers,
                "warranty": [i for i in warranty if i[0] == product.warranty][0][1],
                "deliveryTownTime": [i for i in delivery_town_time if i[0] == product.delivery_town_time][0][1],
                "deliveryTownPrice": delivery_town_price,
                "deliveryCountryTime": [i for i in delivery_country_time if i[0] == product.delivery_country_time][0][1],
                "deliveryCountryPrice": delivery_country_price,
                "productLifeTime": product_life_time,
                "isCashless": is_cashless,
                "isCredit": is_credit,
                "stockStatus": "in_stock",
                "courierDeliveryPrices": courier_delivery_price
            }]

            data.append(product_info)
