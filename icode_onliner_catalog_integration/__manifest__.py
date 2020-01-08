{
    'name': 'ICode - Product Onliner.by publication',
    'version': '1',
    'category': 'Sales',
    'author': 'iCode',
    'website': 'http://icode.by',
    'depends': [
        'stock',
        'product_expiry',
        'techelectro_product',
        'inter_company',
        'techelectro_sale_contract',
        'delivery',
        'stock_picking_batch',
        'techelectro_fleet',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_view_inherit.xml'
        # 'views/product_tree_view_publicize_action_button.xml',
        # 'wizards/product_template_get_product_info_wizard_view.xml'
    ],
}
