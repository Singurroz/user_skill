# -*- coding: utf-8 -*-
{
    'name': "user_skill",

    'summary': """
        User skills""",

    'description': """
        Modulo para guardar el nivel de experiencia de un usuario
    """,

    'author': "Emmanuel Cruz",
    'website': "E",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views_user_skill.xml',
        'views/templates.xml',
        'views/views_res_partner.xml',
        'views/views_skill.xml',
    ],
}
