from odoo import fields, models, api


class IntegrationFields(models.Model):
    _inherit = 'product.product'

    isCashless = fields.Boolean()
    isCredit = fields.Boolean()
    serviceCenters = fields.Char()