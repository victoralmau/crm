# -*- coding: utf-8 -*-
{
    'name': 'Reclamaciones',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'crm', 'delivery'],
    'data': [
        'views/crm_claim_views.xml',
        'views/crm_claim_category_views.xml',
        'views/crm_claim_origin_views.xml',
        'views/crm_claim_stage_views.xml',
        'views/res_partner_views.xml',
        'views/crm_claim_menu.xml',
        'security/ir.model.access.csv',
        'report/crm_claim_report_view.xml',
        'data/crm_claim_data.xml',
        'data/claim_sequence.xml',
    ],
    'installable': True,
    'auto_install': False,    
}