{
    'name': 'ICode - Product Onliner.by publication',
    'description': 'Onliner full API integration',
    'version': '1',
    'category': 'Sales',
    'author': 'iCode',
    'website': 'http://icode.by',
    'depends': [
        'product',
        'base',
        'sale',
        'techelectro_product',
        'techelectro_sale',
        'product_pricelist_prices',
        'techelectro_stock'
    ],
    'data': [
        'data/res_config_parameter.xml',
        'data/onliner_cart_cron.xml',
        'security/ir.model.access.csv',
        'wizards/ship_order_wizard_view.xml',
        'wizards/shop_cancel_wizard_view.xml',
        'wizards/change_order_payment_type_wizard_view.xml',
        'views/product_template_view_inherit.xml',
        'views/product_tree_view_publicize_action_button.xml',
        'views/product_onliner_region_settings_view.xml',
        'views/onliner_cart_view.xml',
        'views/sale_order_onliner_integration.xml',
    ],
    'post_init_hook': 'set_default_courier_delivery_price_ids'
}
