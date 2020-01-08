from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    product_ids = fields.Many2many('product.template', string='Selected Products', compute='_compute_product_statistics')
    product_category = fields.Char()
    vendor = fields.Char()
    model = fields.Char('')
    price = fields.Monetary()
    currency = fields.Many2one('')
    comment = fields.Char()
    producer = fields.Char()
    importer = fields.Char()
    serviceCenters = fields.Char()
    warranty = fields.Char()
    deliveryTownTime = fields.Char()
    deliveryTownPrice = fields.Monetary()
    deliveryCountryTime = fields.Char()
    deliveryCountryPrice = fields.Monetary()
    productLifeTime = fields.Char()
    isCashless = fields.Boolean()
    isCredit = fields.Boolean()
    stockStatus = fields.Char()
    courierDeliveryPrices = fields.Selection()
    product_count = fields.Integer(string='Products Quantity', defaul=0, compute='_compute_product_statistics')

    def _compute_product_statistics(self):

        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        results = self.env['product.template'].read_group(
            [('product_id', 'in', active_ids), ('sale_ok', '!=', False)],
            ['visitor_id', 'page_id', 'url'],
            ['visitor_id', 'page_id', 'url'], lazy=False)
        mapped_data = {}
        for result in results:
            product_info = mapped_data.get(result['product_id'][0],
                                           {'product_count': 0})
            product_info['product_ids_count'] += result['__count']
            product_info['product_count'] += 1
            if result['product_id']:
                product_info['product_ids'].add(result['product_id'][0])
            mapped_data[result['visitor_id'][0]] = product_info
            for selected_product in self:
                product_info = mapped_data.get(selected_product.id,
                                               {'page_count': 0, 'visitor_page_count': 0, 'product_ids': set()})
                selected_product.product_ids = [(6, 0, product_info['product_ids'])]
                selected_product.product_count = product_info['product_count']
        # active_id = self._context.get('active_id')
        # self.number_of_selected_products_for_synchronization = \
        #     len(self._context.get('active_ids', [active_id] if active_id else []))

    # def get_product_info(self):
    #     active_id = self._context.get('active_id')
    #     active_ids = self._context.get('active_ids', [active_id] if active_id else [])
    #     for active_id in active_ids:
    #         self.product_id = self.env['product.template'].search([('product_id', 'in', 'active_ids')]).id
    #         self.product_category = self.env
    #
