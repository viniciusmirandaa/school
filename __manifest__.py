{
    'name': 'School',
    'version': '15.0.0.0',
    'sequence': 2,
    'author': 'Vinicius Silva de Miranda',
    'license': 'LGPL-3',
    'summary': 'School Module',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/school_view.xml',
    ],
    'installable': True,
    'application': True,
}
