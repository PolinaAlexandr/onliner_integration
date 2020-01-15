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
        Product = self.env['product.template']
        product = Product.browse(active_id)
        products = Product.browse(active_ids)
        # for product in products:
        name = product.name


        # invoiced_lines = request.env['account.move.line'].sudo().search(
        #     [('move_id', 'in', order.invoice_ids.ids), ('move_id.invoice_payment_state', '=', 'paid')])
        # products = invoiced_lines.mapped('product_id') | order.order_line.filtered(
        #     lambda r: not r.price_subtotal).mapped('product_id')
        #
        #     # in that case, we should add all download links to the products
        #     # since there is nothing to pay, so we shouldn't wait for an invoice
        # products = order.order_line.mapped('product_id')

        # product_list = self.env['product.template'].browse(active_ids)
        # product_set = product_list.mapped()
        # for product in products:
        # res = products.mapped('product_id')
        # products = self.mapped('product_ids')
        # for active_id in active_ids:
        # names = self.active_ids.mapped('product_ids')
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template.get_product_info_wizard',
            'view_mode': 'form',
            'views': [(form_id, 'form')],
            'context': {
                'default_product_ids': active_ids,
                'default_names': name
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