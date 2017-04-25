# -*- coding: utf-8 -*-
from odoo import fields, models, api
class Sms(models.Model):
    _name='crm.sms'
    date= fields.Date(string='Date')