# -*- codeing:utf-8 -*-
from odoo import models,fields,api

class Appointment(models.Model):
    _name='crm.apm'
    
    description=fields.Char(string='Description',required=True)
    phone=fields.Integer(string="Phone", required=True)
    date=fields.Date(string="Date")
    duration=fields.Datetime(string="Duration")
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
    product_sevice=fields.Char()
    employee=fields.Char()
    type=fields.Selection([
        ('incoming','Incoming call'),
        ('callaway','Call away')
    ],required=True)
    agency_id=fields.Char()
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