from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    # product_category = fields.Char()
    # vendor = fields.Char()
    # model = fields.Char()
    # price = fields.Monetary()
    # currency = fields.Many2one('')
    # comment = fields.Char()
    # producer = fields.Char()
    # importer = fields.Char()
    # serviceCenters = fields.Char()
    # warranty = fields.Char()
    # deliveryTownTime = fields.Char()
    # deliveryTownPrice = fields.Monetary()
    # deliveryCountryTime = fields.Char()
    # deliveryCountryPrice = fields.Monetary()
    # productLifeTime = fields.Char()
    # isCashless = fields.Boolean()
    # isCredit = fields.Boolean()
    # stockStatus = fields.Char()
    # courierDeliveryPrices = fields.Selection()
    product_ids = fields.Many2many('product.template', string='Selected Products')
    names = fields.Char(string='Names')
    product_count = fields.Integer()

    # @api.onchange('product_ids')
    # def _compute_product_ids(self):
    #     product_data = self.env['product.template'].read_group(
    #         [('active_ids', 'in', self.ids)],
    #         ['active_ids'], ['active_ids'])
    #
    #     mapped_data = {datum['active_ids'][0]: datum['product_count'] for datum in product_data}
    #
    #     for product in self:
    #         product.product_count = mapped_data.get(product.id, 0)

    def send_data(self):
        pass

