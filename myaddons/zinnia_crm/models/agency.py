# -*- coding:utf-8 -*-
from odoo import fields, models, api
class Agency(models.Model):
    _name="crm.agency"
    name=fields.Char(string="Name")