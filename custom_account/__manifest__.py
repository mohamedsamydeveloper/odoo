{
'name' : 'Invoicing',
    'version' : '1.2',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base_setup', 'onboarding', 'product', 'analytic', 'portal', 'digest'],
    'data': ['views/account_account_views.xml' ] ,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets' : {'web.assets_backend' ['account/static/src/components/**/*']}
}