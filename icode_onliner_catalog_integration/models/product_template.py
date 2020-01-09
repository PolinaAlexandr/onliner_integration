from odoo import fields, models, api


class IntegrationFields(models.Model):
    _inherit = 'product.template'

    isCashless = fields.Boolean(string='Is Cashless?')
    isCredit = fields.Boolean(string='Is Credit?')
    serviceCenters = fields.Char(string='Service Centers')
