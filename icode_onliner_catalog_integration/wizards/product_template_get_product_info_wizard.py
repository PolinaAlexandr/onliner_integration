"""
TMS Load delivery route cost calculator
"""

import logging

_logger = logging.getLogger(__name__)

from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    product_id = fields.Many2one()
    product_category = fields.Char()
    vendor = fields.Char()
    model = fields.Char('')
    price = fields.Monetary()
    currency = fields.Many2one('')
    comment = fields.Char()
    producer = fields.Char()
    importer = fields.Char()
    warranty = fields.Char()
    deliveryTownTime = fields.Char()
    deliveryTownPrice = fields.Monetary()
    deliveryCountryTime = fields.Char()
    deliveryCountryPrice = fields.Monetary()
    productLifeTime = fields.Char()
    isCashless = fields.Selection()
    isCredit = fields.Selection()
    stockStatus = fields.Char()
    courierDeliveryPrices = fields.Selection()

    def get_product_info(self):
        product_ids = self.env['product.template'].browse(self._context.get('active_ids'))
        if len(product_ids) > 1:
            pass

    # "id": 1,

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

    # def onclick_select_publichase_on_onliner_button(self):
    #     self.ensure_one()
    #     ResPartner = self.env['res.partner']
    #     partner_id = ResPartner.search([('id', '=', self.partner_id.id)], limit=1)
    #     vals = dict(
    #         # country=self.country,
    #         city=self.city,
    #         country_id=self.country_id.id,
    #         email=self.email,
    #         legal_address=self.legal_address,
    #         name=self.name,
    #         phone=self.phone,
    #         street2=self.street2,
    #         street=self.street,
    #         vat=self.vat,
    #         website=self.website,
    #     )
    #     vals = {k: v for k, v in vals.items() if v}
    #     partner_id.write(vals)
    #     view = self.env.ref('base.view_partner_form')
    #     return {
    #         # 'name': 'Task created',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'view_id': view.id,
    #         'res_model': 'res.partner',
    #         'type': 'ir.actions.act_window',
    #         'res_id': partner_id.id,
    #         'context': self.env.context
    #     }
