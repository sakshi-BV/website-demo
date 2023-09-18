# -*- coding: utf-8 -*-
{
    'name': "website_demo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

  
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','website'],
    'license': 'LGPL-3',

    'demo': [
        'demo/demo.xml',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/employee_view.xml',
        'static/src/snippets/banner_static_snippet.xml',
        "static/src/snippets/carousel_static_snippet.xml",
        "static/src/snippets/nav_static_snippet.xml",
        "static/src/snippets/scss_integrated_snippet.xml",
        "static/src/snippets/dynamic_snippet/dynamic_snippet_temp.xml",
        "static/src/snippets/dynamic_snippet/dynamic_snippet.xml",
        'form_template/template_form.xml',
    ],
     'assets': {
       'web.assets_frontend': [
           'website_demo/static/src/scss/custom_styles.scss',
           'website_demo/static/src/snippets/dynamic_snippet/dynamic_snippet.js',
           'website_demo/static/src/snippets/dynamic_snippet/dynamic_snippet_qweb.xml',
            'website_demo/static/src/js/form_data.js',


       ]},
      
    'application': True
}