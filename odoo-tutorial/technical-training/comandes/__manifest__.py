{
"name": "Ventes", # The name that will appear in the App list
"version": "16.0.0", # Version
"application": False, # This line says the module is an App, and not a module
"depends": ["base", "sale"], # dependencies
"data": [
     'security/ir.model.access.csv',
     'views/comanda_views.xml',
     'views/taula_reports.xml'
],
"installable": True,
'license': 'LGPL-3',
}