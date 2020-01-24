from . import models
from . import wizards
from odoo import api, SUPERUSER_ID


# def set_default_courier_delivery_price_ids(cr, registry):
#     env = api.Environment(cr, SUPERUSER_ID, {})
#     product_ids = env['product.template'].search([])
#     product_ids.write({'courier_delivery_price_ids': [(6, 0, env['onliner.region_settings'].search([]).ids)]})
#


