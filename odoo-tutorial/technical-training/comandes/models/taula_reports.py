from odoo import models, fields, tools

class InformeVentesComanda(models.Model):
    _name = 'ventes.comanda.report'
    _description = 'Informe de vendes'
    _auto = False

    comercial = fields.Many2one('res.users', 'Comercial', readonly=True)
    estat = fields.Selection([
        ('draft', 'Pressupost'),
        ('sent', 'Pressupost Enviat'),
        ('sale', 'Comanda de Vendes'),
        ('done', 'Finalitzat'),
        ('cancel', 'Cancel·lat')
    ], string='Estat de la comanda', readonly=True)
    nombre_comandes = fields.Integer('Nombre de comandes', readonly=True)
    import_total = fields.Float('Import total', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'ventes_comanda_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW ventes_comanda_report AS (
                SELECT
                    MIN(so.id) AS id,
                    so.user_id AS comercial,
                    so.state AS estat,
                    COUNT(*) AS nombre_comandes,
                    SUM(so.amount_total) AS import_total
                FROM
                    sale_order so
                GROUP BY
                    so.user_id,
                    so.state
            )
        """)
