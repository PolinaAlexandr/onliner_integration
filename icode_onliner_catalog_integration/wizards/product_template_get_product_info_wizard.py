from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    product_category = fields.Char()
    vendor = fields.Char()
    model = fields.Char()
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
    product_ids = fields.Many2many('product.template', string='Selected Products',
                                   compute='_compute_product_statistics')
    product_count = fields.Integer(string='Products Quantity', defaul=0, compute='_compute_product_statistics')

    def _compute_product_statistics(self):
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        results = self.env['product.template'].read_group(
            [('product_id', 'in', active_ids), ('sale_ok', '!=', False)],
            ['product_id'], lazy=False)
        mapped_data = {}
        for result in results:
            product_info = mapped_data.get(result['product_id'][0],
                                           {'product_count': 0})
            product_info['product_ids_count'] += result['__count']
            product_info['product_count'] += 1
            if result['product_id']:
                product_info['product_ids'].add(result['product_id'][0])
            for selected_product in self:
                product_info = mapped_data.get(selected_product.id,
                                               {'page_count': 0, 'product_ids': set()})
                selected_product.product_ids = [(6, 0, product_info['product_ids'])]
                selected_product.product_count = product_info['product_count']


    # def _add_new_product(self):
    #     pass
    #
    # def _remove_product(self):
    #     pass
         # def _compute_product_statistics(self):
        #     results = self.env['website.track'].read_group(
        #         [('visitor_id', 'in', self.ids), ('product_id', '!=', False)], ['visitor_id', 'product_id'],
        #         ['visitor_id', 'product_id'], lazy=False)
        #     mapped_data = {}
        #     for result in results:
        #         visitor_info = mapped_data.get(result['visitor_id'][0], {'product_count': 0, 'product_ids': set()})
        #         visitor_info['product_count'] += result['__count']
        #         visitor_info['product_ids'].add(result['product_id'][0])
        #         mapped_data[result['visitor_id'][0]] = visitor_info
        #
        #     for visitor in self:
        #         visitor_info = mapped_data.get(visitor.id, {'product_ids': [], 'product_count': 0})
        #
        #         visitor.product_ids = [(6, 0, visitor_info['product_ids'])]
        #         visitor.visitor_product_count = visitor_info['product_count']
        #         visitor.product_count = len(visitor_info['product_ids'])
        # # active_id = self._context.get('active_id')
        # self.number_of_selected_products_for_synchronization = \
        #     len(self._context.get('active_ids', [active_id] if active_id else []))

    # def get_product_info(self):
    #     active_id = self._context.get('active_id')
    #     active_ids = self._context.get('active_ids', [active_id] if active_id else [])
    #     for active_id in active_ids:
    #         self.product_id = self.env['product.template'].search([('product_id', 'in', 'active_ids')]).id
    #         self.product_category = self.env
    #
