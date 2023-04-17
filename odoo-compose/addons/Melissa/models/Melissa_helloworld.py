#Melissa/models/Melissa_helloworld.py
from odoo import api,fields, models

class HelloWorld(models.Model):
    _name= 'helloworld'
    _description = "HelloWorld"
    
    name = fields.Char(string = 'Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')   
    date= fields.Date('Date', required=True)
    mention = fields.Boolean('Mention', required=True)
    