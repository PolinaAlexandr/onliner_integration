{
    'name': 'ICode - Product Onliner.by publication',
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
        'security/ir.model.access.csv',
        'views/product_template_view_inherit.xml',
        'views/product_tree_view_publicize_action_button.xml',
        'views/product_onliner_region_settings_view.xml',
        'wizards/product_template_get_product_info_wizard_view.xml',
    ],
    'post_init_hook': 'set_default_courier_delivery_price_ids'
}
