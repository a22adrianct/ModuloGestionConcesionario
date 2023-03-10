from odoo import models, fields

class Buyer(models.Model):
    _name = 'concesionario.buyer'
    _description = 'Modelo para gestionar los compradores del concesionario'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo electrónico', required=True)
    phone = fields.Char(string='Teléfono')
    cars = fields.Many2many('concesionario.car', string='Coches comprados')

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Este comprador ya existe!'),
    ]
