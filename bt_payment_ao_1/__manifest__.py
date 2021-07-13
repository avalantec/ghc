# -*- coding: utf-8 -*-
# Developer: Carlos Avila.
# Mail: car.josavica@gmail.com
# Boostech CR
# 21.07.13

{
    'name' : 'Referencia de pago',
    'version' : '21.07.13',
    'summary': 'Registrar información de referencia del pago',
    'sequence': 0,
    'description': """
Contiene
====================

    Permite registrar la información de referencia del pago:
    * N. depósito
    * N. Transferencia
    * N. SINPE Móvil
    * Otros
    
    """,
    'category': 'AddOns',
    'author': "Boostech CR",
    'website': 'https://boostechcr.com/',
    'images' : [
    ],
    'depends' : [
        'account',
    ],
    'data': [
        'views_inherits/views_bt_account_payment_register.xml',
        'views_inherits/views_bt_account_payment.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
