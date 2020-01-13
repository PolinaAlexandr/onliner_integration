from odoo import fields , models, api


class IntegrationFields(models.Model):
    _inherit = 'product.template'

    isCashless = fields.Boolean(string='Is Cashless?')
    isCredit = fields.Boolean(string='Is Credit?')
    serviceCenters = fields.Char(string='Service Centers')
    delivery_country_id = fields.Many2one('res.country', ' Country',
                                          default=lambda self: self.env['res.country'].search(['code', '=', 'BY']))
    # delivery_town_price =
    # courierDeliveryPrices = fields.Many2many('product.template', 'product.template.', )
