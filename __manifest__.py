{
    'name': 'sid_sale_order_margin_costs',
    'version': '1.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Campos en vista form para visualizar margen neto tras costes adicionales no reflejados en líneas de venta',
    'description': 'Campos en vista form para visualizar margen neto tras costes adicionales no reflejados en líneas de venta',
    'author': 'oscarsidsa81',
    'depends': ['base','sale_management'],
    'data': [
        'views/sid_sale_order_margin_costs.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}