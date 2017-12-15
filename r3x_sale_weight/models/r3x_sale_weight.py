#Part of RU3IX.See __manifest__.py file for full copyright and licensing details.
from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class sale_order(models.Model):
    """ Sale order """
    _inherit = 'sale.order'

    @api.multi
    def _cal_weight(self):
        """ Calculate the sale weight """
        for sale in self:
            self.weight = 0.00
            for line in sale.order_line:
                self.weight += line.th_weight

    weight = fields.Float(compute='_cal_weight', string='Weight', \
            digits=dp.get_precision('Stock Weight'))

class sale_order_line(models.Model):
    """ Sale order Lines"""
    _inherit = 'sale.order.line'
    
    th_weight = fields.Float(string='Weight', readonly=True, states={'draft': [('readonly', False)]}, digits=dp.get_precision('Stock Weight'))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
