import requests
import json
from odoo import fields, models, api, exceptions, _


class ShopCancelOrderWizard(models.TransientModel):
    _name = 'sale.order.shop.cancel.order.wizard'

    reason_id = fields.Integer()
    comment = fields.Char()

    # def get_shop_cancel_order_reasons(self):
    #     url = 'https://cart.api.onliner.by/resources/shop-cancel-reasons'
    #     headers = {
    #         'Accept': 'application/json',
    #     }
    #     response_request = requests.get(url=url, headers=headers)
    #     response_summary = json.loads(response_request.content.decode('utf-8'))
    #     if response_summary:
    #         for item in response_summary:
    #             self.reason_id = item['id']
    #             self.comment = item['text']
    #     else:
    #         pass

    @api.model
    def shop_cancel_order(self):
        pass
        # active_id = self._context.get('active_id')
        # order = self.env['sale.order'].browse(active_id)
        # key = order.key
        # url = 'https://cart.api.onliner.by/orders/{}'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "reason": {
        #       "id": self.self.id
        #       "comment": self.comment
        #     }
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request