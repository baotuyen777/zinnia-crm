# -*- coding: utf-8 -*-
{
    'name': "zinnia_CRM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       Module CRM
    """,

    'author': "Zinia",
    'website': "http://www.zinnia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/crm.xml',
        'views/partner.xml',
        'views/landing_page_source.xml',
        'views/appointment.xml',
        'views/request.xml',

        # 'views/session_board.xml',
        # 'views/openacademy.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}