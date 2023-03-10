from odoo import models, fields, api

class Car(models.Model):
    _name = 'concesionario.car'
    _description = 'Modelo para gestionar los coches del concesionario'

    name = fields.Char(string='Nombre', required=True)
    brand = fields.Char(string='Marca', required=True)
    model = fields.Char(string='Modelo', required=True)
    year = fields.Integer(string='Año', required=True)
    price = fields.Float(string='Precio', required=True)
    description = fields.Text(string='Descripción')
    image = fields.Binary(string='Imagen')

    @api.depends('brand', 'model')
    def _compute_name(self):
        for car in self:
            car.name = '{} {}'.format(car.brand or '', car.model or '')

    _sql_constraints = [
        ('unique_brand_model', 'unique(brand, model)', 'Este coche ya existe!'),
    ]
