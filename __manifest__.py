{
    'name': 'Restricted List Price',
    'version': '1.3',
    'summary': 'Restricts visibility of the list_price field using a custom group.',
    'description': 'Makes the list_price field completely invisible to non-members of the "Price Viewers" group.',
    'author': 'Alphaqueb Consulting',
    'depends': ['product', 'sale_management'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml'
    ],
    'installable': True,
    'application': False,
}