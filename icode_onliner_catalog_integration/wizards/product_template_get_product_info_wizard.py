"""
TMS Load delivery route cost calculator
"""

import logging

_logger = logging.getLogger(__name__)

from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'

    product_id = fields.Many2one()
    product_category = fields.Char()
    vendor = fields.Char()
    model = fields.Char('')
    price = fields.Monetary()
    currency = fields.Many2one('')
    comment = fields.Char()
    producer = fields.Char()
    importer = fields.Char()
    warranty = fields.Char()
    deliveryTownTime = fields.Char()
    deliveryTownPrice = fields.Monetary()
    deliveryCountryTime = fields.Char()
    deliveryCountryPrice = fields.Monetary()
    productLifeTime = fields.Char()
    isCashless = fields.Selection()
    isCredit = fields.Selection()
    stockStatus = fields.Char()
    courierDeliveryPrices = fields.Selection()

    def get_product_info(self):
        active_id = self._context.get('active_id')
        active_ids = self._context.get('active_ids', [active_id] if active_id else [])
        for active_id in active_ids:
            self.product_id = self.env['product.template'].search([('product_id', 'in', 'active_ids')]).id
            self.product_category = self.env

