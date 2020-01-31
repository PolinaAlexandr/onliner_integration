import requests
import json
from odoo import fields, models, api, exceptions, _


class ShopCancelOrderWizard(models.TransientModel):
    _name = 'sale.order.shop.cancel.order.wizard'

    reason_id = fields.Integer()
    comment = fields.Char()

    @api.model
    def shop_cancel_order(self):
        pass
        # active_id = self._context.get('active_id')
        # order_id = self.env['sale.order'].browse(active_id).id
        # key = order_id.key
        # url = 'https://cart.api.onliner.by/oreders/{}'.format(key)
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