# -*- coding: utf-8 -*-
{
    'name': 'HelpDesk Extension',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'category': 'Helpdesk',
    'summary': 'Helpdesk Extension',
    'website': 'http://www.serpentcs.com',
    'license': 'AGPL-3',
    'description': """  """,
    'version': '13.0.1.0.0',
    'depends': ['helpdesk', 'product'],
    'data': [
        'views/helpdesk_view.xml',
        'views/product_view.xml',
    ],
    # 'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
