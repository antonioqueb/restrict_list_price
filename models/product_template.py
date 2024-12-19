from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    list_price_restricted = fields.Float(
       string='Precio de Venta',
       compute='_compute_list_price_restricted',
       readonly=True,
       store=True,
       help="Precio de venta, visible solo para miembros del grupo 'Price Viewers'"
    )


    @api.depends('list_price')
    def _compute_list_price_restricted(self):
       for record in self:
          if self.env.user.has_group('restrict_list_price.group_price_viewers'):
                record.list_price_restricted = record.list_price
          else:
                record.list_price_restricted = False # no mostrar el campo a usuarios no autorizados.