 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class libreria_categoria(models.Model):
     _name = 'libreria.categoria'
     name = fields.Char(string="Nombre", required=True, help="Introduce el nombre de una categoría")
     description = fields.Text(string="Descripcion")

class libreria_libro(models.Model):
    _name = 'libreria.libro'
    name = fields.Char(string="Titulo", required=True, help="Introduce el titulo de un libro")
    precio=fields.Float(string="Precio")
    ejemplares=fields.Integer(string="Ejemplares")
    fecha=fields.Date(string="Fecha de compra")
    segmano=fields.Boolean(string="Segunda mando")
    estado=fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default="0")
