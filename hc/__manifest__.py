# -*- coding: utf-8 -*-
{
    'name': "hc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management', 'stock', 'account_accountant', 'crm','l10n_cr_zones'],

    # always loaded
    'data': [
        'views/user_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',  
        'views/product_product.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/hc_state.xml',
        'views/access_views.xml',
        'views/stock_quant.xml',
        'views/account_move.xml',

    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
