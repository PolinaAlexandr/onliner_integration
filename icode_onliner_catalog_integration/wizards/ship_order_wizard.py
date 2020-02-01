import requests
import json
from odoo import fields, models, api, exceptions, _


class ShipOrderWizard(models.TransientModel):
    _name = 'sale.order.ship.order.wizard'

    delivery_comment = fields.Char()

    @api.model
    def ship_order(self):
        pass
        # active_id = self._context.get('active_id')
        # order = self.env['sale.order'].browse(active_id)
        # key = order.key
        # url = 'https://cart.api.onliner.by/oreders/{}'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "delivery_comment": self.delivery_comment
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request
