from odoo import models, fields, api

class Sale(models.Model):
    _name = 'concesionario.sale'
    _description = 'Modelo para gestionar las ventas de coches del concesionario'

    car_id = fields.Many2one('concesionario.car', string='Coche', required=True)
    buyer_id = fields.Many2one('concesionario.buyer', string='Comprador', required=True)
    date = fields.Date(string='Fecha', required=True)
    price = fields.Float(string='Precio', required=True)

    @api.depends('car_id', 'buyer_id')
    def _compute_name(self):
        for sale in self:
            sale.name = '{} - {}'.format(sale.car_id.name or '', sale.buyer_id.name or '')

    _sql_constraints = [
        ('unique_car_buyer', 'unique(car_id, buyer_id)', 'Este coche ya ha sido vendido a este comprador!'),
    ]
