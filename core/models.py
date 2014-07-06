# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.sites.models import Site
from sorl.thumbnail import ImageField

from team import models as tm

### 
# Site 
# Django site related to team
###
class TeamSite(Site):
	team = models.ForeignKey(tm.Team)

	objects = Site.objects

###
# Sponsors and ads 
###
class Sponsor(models.Model): 
	title = models.CharField(max_length=255)
	url = models.URLField()
	logo = ImageField(upload_to='sponsors/')
	site = models.ForeignKey(TeamSite)

	def __unicode__(self): 
		return u'%s' % self.title