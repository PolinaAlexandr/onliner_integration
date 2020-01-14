import json
import requests

from requests import Session
from odoo import fields, models, api


class OnlinerCatalog(models.Model):
    _inherit = 'product.template'

    def publicize_on_onliner(self):
        form_id = self.env.ref('icode_onliner_catalog_integration.product_template_get_product_info_wizard_view').id
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', active_id if active_id else [])
        # product_id = self.env['product.template'].search([('product_id', '=', active_id)]).id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template.get_product_info_wizard',
            'view_mode': 'form',
            'views': [(form_id, 'form')],
            'context': {
                'default_product_ids': active_ids,
                'default_sale_ok': False,
            },
            'target': 'new'}

    #     summary_url = 'https://b2bapi.onliner.by/positions/{}?access-token={}'
    #     headers = {'Content-Type': 'application/json'
    #     token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
    #     # response_egr = requests.get(egr_url.format(unp, token))
    #     # res_egr = json.loads(response_egr.content.decode('utf-8'))
    #     response_summary = requests.get(summary_url.format(unp, token))
    #     res_summary = json.loads(response_summary.content.decode('utf-8'))
    #     # print(res_egr)
    #     # return res_egr
    #     print(res_summary)
    #     return res_summary

    #     self.ensure_one()
        # for active_id in active_ids:
        #     product_data = self.env.get()
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