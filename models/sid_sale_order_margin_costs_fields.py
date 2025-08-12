from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    margen_neto = fields.Float(
        string="Margen Neto",
        compute="_compute_margen_neto",
        help="Base imponible que queda por entregar",
        store=True,
        readonly=True,
        digits=(16,4),
        tracking=True,
        help="Margen revisado teniendo en cuenta los Costes Adicionales"
    )

    costes_adicionales = fields.Monetary(
        string="Costes Adicionales",
        default=0.0,
        store=True,
        readonly=False,
        tracking=True,
        currency_field='currency_id',
        help="Costes adicionales no reflejados en los costes de las líneas de venta",
    )

    # === MÉTODOS ===

    @api.depends('margin', 'costes_adicionales', 'amount_untaxed', 'margin_percent')
    def _compute_margen_neto(self):
        for record in self :
            margin = record.margin or 0.0
            extra = record.costes_adicionales or 0.0
            base = record.amount_untaxed or 0.0

            # Si no hay base imponible, evitar división y usar el % de margen existente
            if base <= 0 :
                record.margen_neto = record.margin_percent or 0.0
                continue

            # Si hay costes adicionales, recalculamos sobre la base imponible
            if extra > 0 :
                record.margen_neto = (margin - extra) / base
            else :
                # Si no hay costes adicionales, mantenemos el valor existente de margen_percent (ya es un ratio en sale_margin)
                record.margen_neto = record.margin_percent or (margin / base if base else 0.0)