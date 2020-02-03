import requests
import json
from odoo import fields, models, api, exceptions, _

PAYMENT_TYPES = [
    ('1', 'cash'),
    ('2', 'terminal'),
    ('3', 'cashless')
]


class ChangeOrderPaymentTypeWizard(models.TransientModel):
    _name = 'sale.order.change.order.payment.type.wizard'

    payment_type = fields.Selection(PAYMENT_TYPES)

    @api.model
    def change_order_payment_type(self):
        pass
        # active_id = self._context.get('active_id')
        # order = self.env['sale.order'].browse(active_id)
        # key = order.key
        # state = order.payment_type
        # url = 'https://cart.api.onliner.by/orders/{}/change-payment-type'.format(key)
        # token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': 'Bearer {}'.format(token),
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     "payment_type": self.payment_type
        # }
        # json_data = json.dumps(data)
        # response_request = requests.patch(url, data=json_data, headers=headers)
        # return response_request
