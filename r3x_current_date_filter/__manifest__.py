##############################################################################
#    Copyright (c) 2017 RU3IX Pvt. Ltd.
#    (http://www.ru3ix.com.au)
#    info@ru3ix.com.au
#
##############################################################################
{
    'name': 'Today Filters',
    'version': '1.0',
    'author': 'Aspire Apps',
    'website': 'www.ru3ix.com.au',
    'category': 'base',
    'summary': 'Today Filters on Search Views',
    'description':  """This Module will set Today filter in search view in following menus.
                        * Sales Quotations & Purchase Quotations
                        * Sales Orders
                        * Purchase Orders
                        * Stock Operations (Delivery Orders)
                        * Customer Invoices
                        * Supplier Invoices (Vendor Bills)
                        * Sales Receipts
                        * Purchase Receipts
                        * Sales Payment
                        * Purchases Payment""",
    'price': 20,
    'currency': 'EUR',
    'depends': ['account_voucher', 
        'stock_account', 
        'sale_management', 
        'purchase'],
    'data': ['views/current_date_view.xml'],
    'installable': True,
    'auto_install': False,
}
