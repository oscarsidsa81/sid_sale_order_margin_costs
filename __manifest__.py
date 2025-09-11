{
    'name': 'sid_sale_order_margin_costs',
    'version': '1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Campos en vista tree "Pedidos para control de facturación',
    'description': 'Campos calculados a partir de líneas de ventas y productos'
                   ' concretos para separar las diferentes carteras de '
                   'facturación de un contrato o pedido',
    'author': 'oscarsidsa81',
    'depends': ['base','sale_management'],
    'data': [
        'views/sid_sale_order_margin_costs.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}