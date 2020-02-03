import requests
import json
from odoo import fields, models, api, exceptions, _

STATUSES = [
    ('new', 'new'),
    ('processing', 'processing'),
    ('confirmed', 'confirmed'),
    ('shipping', 'shipping'),
    ('delivered', 'delivered'),
    ('shop_canceled', 'shop canceled')
]


class SaleOrderIntegrationFields(models.Model):
    _inherit = 'sale.order'

    key = fields.Char('Onliner Order Key', readonly="1")
    onliner_delivery_state = fields.Selection(STATUSES)
    payment_type = fields.Char(string='Payment Type', readonly=1)

    @api.model
    def process_order(self):
        pass
        # active_id = self._context.get('active_id')
        # order_id = self.env['sale.order'].browse(active_id).id
        # key = order_id.key
        # url = 'https://cart.api.onliner.by/orders/{}'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "status": "processing"
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request
        # response_summary = json.loads(response_request.content.decode('utf-8'))

    @api.model
    def confirm_order(self):
        pass
        # active_id = self._context.get('active_id')
        # order_id = self.env['sale.order'].browse(active_id).id
        # key = order_id.key
        # url = 'https://cart.api.onliner.by/orders/{}'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "status": "confirmed"
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request
        # response_summary = json.loads(response_request.content.decode('utf-8'))

    @api.model
    def order_delivered(self):
        pass
        # active_id = self._context.get('active_id')
        # order_id = self.env['sale.order'].browse(active_id).id
        # key = order_id.key
        # url = 'https://cart.api.onliner.by/orders/{}'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "status": "delivered"
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request
