# -*- coding: utf-8 -*-
{
    'name': "Sale_order payment methods",

    'summary': """
        This is a short summary of the new custom module Sale_order!""",

    'description': """
        The purpose of this module is to learn and understand how odoo works, and we will get there in a second!
    """,

    'author': "Atrivia",
    'website': "webpage",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}
