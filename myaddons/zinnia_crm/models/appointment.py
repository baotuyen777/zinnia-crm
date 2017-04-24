# -*- codeing:utf-8 -*-
from odoo import models,fields,api

class Appointment(models.Model):
    _name='crm.apm'
    
    description=fields.Char(string='Description',required=True)
    phone=fields.Char(string="Phone", required=True)
    date=fields.Date(string="Date")
    duration=fields.Char(string="Duration", default="01:00")
    purpose=fields.Selection([
        ('appointment_th','appointment TH'),
        ('appointment_tv', 'appointment TV'),
        ('consult', 'Colsult'),
    ],required=True)
    field=fields.Selection([
        ('advtech','Advance Technology'),
        ('spa','Spa'),
    ],required=True)
    contact_id=fields.Many2one('res.partner', string='Contact')
    rate=fields.Selection([
        ('success','Success'),
        ('potential','Potential'),
    ])
    product_id=fields.Many2one('crm.product',string ='Product service')
    employee=fields.Char()
    call_type=fields.Many2one('crm.call_type', string="Call type")
    agency_id=fields.Many2one('crm.agency',string='Agency')
    branch = fields.Selection([
        ('thucuc', 'Thu Cuc Hospital'),
        ('228tayson', '228 Tay son'),
        ('57nguyenkhachieu', '57 Nguyen Khac Hieu'),
    ])
    maketing_channel = fields.Selection([
        ('email', 'Email'),
        ('sms', 'Sms'),
        ('facebook', 'Facebook')
    ])
    phone_number=fields.Char(string='Phone number')
    request_id=fields.Many2one('crm.request')
    description_detail=fields.Text()
    # partner_ids = fields.One2many('res.partner', 'lps_id', string="Partner")
    history_id =fields.One2many('crm.history','apm_id',string='History')