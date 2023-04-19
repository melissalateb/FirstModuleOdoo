#Melissa/__maifest__.py
{
    'name' : 'Melissa',
    'summary' : '',
    'author' :"Melissa",
    'description' : 'Module2 Hello World',
    'website':'https://melissa.com',
    'version': '1.0',
    'depends': ['base' ,'mail'],
    'data': [
        'views/hello_world_views.xml',
        'views/partner_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/src/img/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'GPL-3',
}