# -*- coding: utf-8 -*-

from django.db import models

###
# Team
###
class Championship(models.Model):
	name = models.CharField("Nom", max_length=255)

	def __unicode__(self):
		return u'%s' % self.name

class Team(models.Model):
	name = models.CharField("Nom", max_length=255)
	abbr = models.CharField("Abbréviation", max_length=10)
	picture = models.ImageField("Image", upload_to="media/teams/", blank=True, null=True)
	championship = models.ForeignKey("Championship", blank=True, null=True)

	def __unicode__(self):
		return u'%s' % self.name

###
# Players
###
class Player(models.Model):
	LEFT_HANDED = 1
	RIGHT_HANDED = 2
	BOTH_HANDED = 3
	FEET_CHOICES = (
        (LEFT_HANDED, 'Gaucher'),
        (RIGHT_HANDED, 'Droitier'),
        (BOTH_HANDED, 'Ambidextre'),
    )
	firstname = models.CharField("Prénom", max_length=255)
	lastname = models.CharField("Nom", max_length=255)
	birthdate = models.DateField("Date de naissance", blank=True, null=True)
	birthplace = models.CharField("Lieu de naissance", max_length=255, blank=True, null=True)
	number = models.IntegerField("Numéro de maillot", blank=True, null=True)
	picture = models.ImageField("Image", upload_to="media/players/", blank=True, null=True)
	feet = models.IntegerField("Pied de prédilection", choices=FEET_CHOICES, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	team = models.ForeignKey('Team', blank=True, null=True)
	positions = models.ManyToManyField('Position', through='PlayerPosition')
	skills = models.ManyToManyField('Skill', through='PlayerSkill')

	def __unicode__(self):
		return u'%s %s' % (self.firstname, self.lastname)

	def get_main_position(self): 
		if self.positions.all().count() == 0:
			return null
		return self.positions.all()[0]

###
# Positions
# Players capabilities
###
class Position(models.Model):
	GOALKEEPER = 1
	DEFENDER = 2
	MIDFIELDER = 3
	STRIKER = 4
	FEET_CHOICES = (
        (GOALKEEPER, 'Gardien'),
        (DEFENDER, 'Défenseur'),
        (MIDFIELDER, 'Milieu'),
        (STRIKER, 'Attaquant'),
    )
	label = models.CharField("Libellé", max_length=255)
	abbr = models.CharField("Abbreviation", max_length=4)
	type = models.IntegerField(choices=FEET_CHOICES)

	def __unicode__(self):
		return u'%s' % self.abbr

class PlayerPosition(models.Model): 
	preference = models.IntegerField()
	position = models.ForeignKey('Position')
	player = models.ForeignKey('Player')


###
# Skills
# Different skills and types
###
class Skill(models.Model):
	label = models.CharField("Libellé", max_length=255)
	abbr = models.CharField("Abbréviation", max_length=4)
	order = models.IntegerField()
	type = models.ForeignKey('SkillType')

	def __unicode__(self):
		return u'%s' % self.label

class SkillType(models.Model):
	label = models.CharField("Libellé", max_length=255)
	order = models.IntegerField()

	def __unicode__(self):
		return u'%s' % self.label

class PlayerSkill(models.Model):
	value = models.FloatField()
	skill = models.ForeignKey('Skill')
	player = models.ForeignKey('Player')
