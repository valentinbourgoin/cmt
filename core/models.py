# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.sites.models import Site

from team import models as tm

### 
# Site 
# Django site related to team
###
class TeamSite(Site):
	team = models.ForeignKey(tm.Team)

