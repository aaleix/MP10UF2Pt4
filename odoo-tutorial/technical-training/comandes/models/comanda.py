from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_lines_count = fields.Integer(string="Productes diferents a la comanda", compute='_compute_order_lines_count')
    correu_client = fields.Char(string='Correu del client')


    def _compute_order_lines_count(self):
        for order in self:
            order.order_lines_count = len(order.order_line)



