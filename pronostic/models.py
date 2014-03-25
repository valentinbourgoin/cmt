# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from team import models as tm


###
# Matchday
# 
###
class MatchDay(models.Model):
	championship = models.ForeignKey(tm.Championship)
	label = models.CharField("Libellé", max_length=255)

	def __unicode__(self):
		return u'%s - %s' % (self.championship, self.label)

class Match(models.Model):
	match_day = models.ForeignKey(MatchDay)
	date_min = models.DateTimeField("Date de début de soumission", null=True, blank=True)
	date_max = models.DateTimeField("Date de fin de soumission", null=True, blank=True)
	date = models.DateTimeField("Date du match",)
	team_home = models.ForeignKey(tm.Team, related_name="team_home")
	team_away = models.ForeignKey(tm.Team, related_name="team_away")

	def __unicode__(self):
		return u'%s - %s' % (self.team_home, self.team_away)

###
# Pronostic
# Pronostic for score, goals and positions for each players
###
class Pronostic(models.Model):
	match = models.ForeignKey(Match)
	user = models.ForeignKey(User)
	score_home = models.IntegerField()
	score_away = models.IntegerField()
	points = models.FloatField(default=0)
	positions = models.ManyToManyField(tm.Position, through='PronosticPosition')
	scorers = models.ManyToManyField(tm.Player, through='PronosticGoal')

class PronosticPosition(models.Model):
	pronostic = models.ForeignKey(Pronostic)
	player = models.ForeignKey(tm.Player)
	position = models.ForeignKey(tm.Position)

class PronosticGoal(models.Model):
	pronostic = models.ForeignKey(Pronostic)
	player = models.ForeignKey(tm.Player)
	goal_number = models.IntegerField()

###
# Results
# Actual result for match
###
class Result(models.Model):
	match = models.ForeignKey(Match)
	score_home = models.IntegerField()
	score_away = models.IntegerField()
	positions = models.ManyToManyField(tm.Position, through='ResultPosition')
	scorers = models.ManyToManyField(tm.Player, through='ResultGoal')

class ResultPosition(models.Model):
	result = models.ForeignKey(Result)
	player = models.ForeignKey(tm.Player)
	position = models.ForeignKey(tm.Position)

class ResultGoal(models.Model):
	result = models.ForeignKey(Result)
	player = models.ForeignKey(tm.Player)
	goal_number = models.IntegerField()