import json
import requests

from requests import Session
from odoo import fields, models, api


class OnlinerCatalog(models.Model):
    _inherit = 'product.template'

    def publicize_on_onliner(self):
        form_id = self.env.ref('icode_onliner_catalog_integration.product_template_get_product_info_wizard_view').id
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        product_count = len(active_ids)
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        product_info = {}
        for product in products:
            product_info = {
                "id": product.id,
                "category": product.categ_id.name,
                "vendor": product.producer_name.id,
                "model": product.name,
                "price": product.list_price,
                "currency": "BYN",
                "comment": product.extra_description,
                "producer": "Foxconn,No.2,2nd Donghuan Road,10th Yousong Industrial District",
                "importer": product.customer_info_ids,
                "serviceCenters": product.service_centers,
                # "warranty": product.self._fields['warranty'],
                "warranty": product.warranty,
                "deliveryTownTime": product.delivery_town_time,
                "deliveryTownPrice": product.delivery_town_price,
                "deliveryCountryTime": product.delivery_country_time,
                "deliveryCountryPrice": product.delivery_country_price,
                "productLifeTime": product.exploitation_period,
                "isCashless": product.is_cashless,
                "isCredit": product.is_credit,
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
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template.get_product_info_wizard',
            'view_mode': 'form',
            'views': [(form_id, 'form')],
            'context': {
                'default_product_ids': active_ids,
                'default_names': product_info,
                'default_product_count': product_count,
            },
            'target': 'new'}

    #     self.ensure_one()
        # for active_id in active_ids:
        #     exporter_dict = {
        #         "id": 1,
        #         "category": "MP3-плееры",
        #         "vendor": "Apple",
        #         "model": "iPod nano 16Gb (7th generation)",
        #         "price": "20.00",
        #         "currency": "BYN",
        #         "comment": "Ваш комментарий",
        #         "producer": "Foxconn,No.2,2nd Donghuan Road,10th Yousong Industrial District",
        #         "importer": "ООО Музтрейд, г.Минск, ул. Кропоткина, 12\r\nООО Плеерсервис, г.Гомель, ул. Платонова, 16",
        #         "serviceCenters": "ООО Музсервис, г.Минск, ул. П. Бровки, 5\r\nООО Плеерсервис, г.Гомель, ул. Платонова, 16",
        #         "warranty": "12",
        #         "deliveryTownTime": 1,
        #         "deliveryTownPrice": "1.00",
        #         "deliveryCountryTime": 5,
        #         "deliveryCountryPrice": "2.00",
        #         "productLifeTime": 36,
        #         "isCashless": "нет",
        #         "isCredit": "нет",
        #         "stockStatus": "in_stock",
        #         "courierDeliveryPrices": {
        #             "region-1": {
        #                 "type": "custom",
        #                 "amount": "2.99"
        #             },
        #             "region-2": {
        #                 "type": "no"
        #             }
        #         }
        #     }