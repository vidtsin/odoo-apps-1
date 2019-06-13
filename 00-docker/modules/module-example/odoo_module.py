# -*- coding: utf-8 -*-

""" Ceci est le fichier de notre module contenant un modele de notre
base de donnee. On peut egalement y ajouter nos controlleurs mais tout 
depend de la structure de notre module """

from openerp import fields, models

class Person(models.Model):
    _name = 'person.model'
    nom = fields.Char("Nom", required=True)
    prenom = fields.Char("Prenom", required=True)