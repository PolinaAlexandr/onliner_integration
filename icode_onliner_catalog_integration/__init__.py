from . import models
from odoo import api, SUPERUSER_ID


def set_default_courier_delivery_price_ids(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    delivery_vals = env['onliner.region_settings'].search([])
    product_ids = env['product.template'].search([])
    result = []
    if delivery_vals:
        for delivery_val in delivery_vals:
            result.append((0, 0, {
                'name': delivery_val.name,
                'delivery_type': delivery_val.delivery_type,
                'price': delivery_val.price,
                }))
        product_ids.update({'courier_delivery_price_ids': result})
        return product_ids
