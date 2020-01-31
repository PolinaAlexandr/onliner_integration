from odoo import fields, models, api

STATUSES = [
    ('new', 'new'),
    ('processing', 'processing'),
    ('confirmed', 'confirmed'),
    ('shipping', 'shipping'),
    ('delivered', 'delivered'),
    ('shop_canceled', 'shop canceled')
]

PAYMENT_TYPES = [
    ('1', 'cash'),
    ('2', 'terminal'),
    ('3', 'cashless')
]


class SaleOrderIntegrationFields(models.Model):
    _inherit = 'sale.order'

    key = fields.Char('Onliner Order Key')
    onliner_delivery_state = fields.Selection(STATUSES)

    @api.model
    def process_order(self):
        pass

    @api.model
    def confirm_order(self):
        pass
    # PATCH / orders / qz2wa
    # Authorization: bearer < token >
    # Accept: application / json;
    # charset = utf - 8
    # Content - Type: application / json;
    # charset = utf - 8
    # {
    #     "status": "confirmed"
    # }

    @api.model
    def ship_order(self):
        pass

    # PATCH / orders / qz2wa
    # Authorization: bearer < token >
    # Accept: application / json;
    # charset = utf - 8
    # Content - Type: application / json;
    # charset = utf - 8
    # {
    #     "status": "shipping",
    #     "delivery_comment": "Курьер будет у вас с 15:00 до 18:00"
    # }

    @api.model
    def order_delivered(self):
        pass
        # PATCH / orders / qz2wa
        # Authorization: bearer < token >
        # Accept: application / json;
        # charset = utf - 8
        # Content - Type: application / json;
        # charset = utf - 8
        # {
        #     "status": "confirmed"
        # }

    @api.model
    def shop_cancel_order(self):
        pass

    # PATCH / orders / qz2wa
    # Authorization: bearer < token >
    # Accept: application / json;
    # charset = utf - 8
    # Content - Type: application / json;
    # charset = utf - 8
    # {
    #     "status": "shop_canceled",
    #     "reason": {
    #         "id": 1,
    #         "comment": "товара нет в наличии"
    #     }
    # }
