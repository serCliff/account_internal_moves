# -*- coding: utf-8 -*-
{
    'name': "Account Internal Moves",

    'summary': """
        New Menu to manage internal moves on you companies""",

    'description': """
        This module give you a better way to make internal transfers between journals
        - Allow to your users make internal transfers since pos.session kanban
        - Give you a new menu on Account/Adviser/Internal transfers to show the internal transfers


        IMAGES: 

        The button that appears on pos.session kanban to make internal transfers
        https://github.com/serCliff/account_internal_moves/blob/10.0/img/pos_session.png


        The account.payment form to make a internal transfer
        https://github.com/serCliff/account_internal_moves/blob/10.0/img/account_payment.png


        STILL MISSING
        
        - Not transated
        - Without seccurity groups

        git: https://github.com/serCliff/account_internal_moves
    """,


    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_payment_views.xml',
        'views/account_pos_moves_views.xml',
    ],
}