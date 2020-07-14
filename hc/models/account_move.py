# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    #warehouse_id = fields.Many2one(string='Almacen',related='stock.warehouse',store = True) 
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse",store = True)