#Melissa/models/Melissa_helloworld.py
from odoo import api,fields, models
import logging

_logger = logging.getLogger(__name__) #enregistrer le message dans le journal des logs niveau INFO

class HelloWorld(models.Model):
    _name= 'helloworld'
    _description = "HelloWorld"
    _inherit =["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string = 'Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')   
    date= fields.Date('Date', required=True)
    mention = fields.Boolean('Mention', required=True)    
    auType = fields.Selection(selection=[('type1', 'Bonjour'),('type2', 'Bonsoir'),], string='Politesse', default= 'Bonjour')
    logger = fields.Text(string='Logger')
    # note_ids = fields.One2many('Melissa.note', 'partner_id', string='Notes')
    # activity_ids = fields.One2many(comodel_name='activity', string='Activities')
    # message_ids = fields.One2many(comodel_name='message', inverse_name='partner_id', string='Messages')

    
    def log_action(self): # definit un log action pour un modele , pour chaque enregistremet on cree un message contenant les informations 
        for record in self:
            message = "Action '%s' with Partner '%s' on %s, Selection: %s, Checkbox: %s" % (
                record.name, record.partner_id.name, record.date, record.auType, record.mention)
            _logger.info(message)
    
    
