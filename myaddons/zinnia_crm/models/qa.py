# -*- coding:utf-8 -*-

from odoo import fields, models, api
class qa(models.Model):
    _name = 'crm.qa'
    name=fields.Char(string='Name')
