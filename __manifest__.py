# -*- coding: utf-8 -*-
{
    'name': "Account Internal Moves",

    'summary': """
        New Menu to manage internal moves on you companies""",

    'description': """
        - Added a improved view with a new field that ease the internal money operations
        - Added a new menu on Account/Adviser/Internal transfers

        STILL MISSING
        - Not transated
        - Without seccurity groups

        git: 
    """,


    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_payment_views.xml',
        'views/account_move.xml',
    ],
}