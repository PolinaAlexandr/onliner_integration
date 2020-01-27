from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'
    product_ids = fields.Many2many('product.template', string='Selected Products')
    names = fields.Char(string='Names')

    def send_data(self):
        pass