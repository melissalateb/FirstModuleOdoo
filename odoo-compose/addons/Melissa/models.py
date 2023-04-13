# -*- coding: utf-8 -*-   declaration d'encodage
from odoo import models ,fields # models contient la classe et fields les bases predefinies : char, integer,boolean
# . signifie que le module est dans le même dossier que le fichier actuel.
class HelloWorld(models.Model): #classe hello world qui herite de la classe models.Model
    _name = 'hello.world' #definit le nom du modele dans la bd d'odoo
    
    name = fields.Char(default='Hello World!') #defini un champ name qui est de type char qui a 'Hello World!' comme defaut

