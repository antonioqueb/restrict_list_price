{
    'name': 'Restricted List Price',
    'version': '1.2',
    'summary': 'Restricts visibility of the list_price field using a custom group.',
    'description': 'Makes the list_price field visible only to members of the "Price Viewers" group.',
    'author': 'Alphaqueb Consulting',
    'depends': ['product', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'installable': True,
    'application': False,
}