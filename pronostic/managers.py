from datetime import datetime    

from django.db import models
from django.db.models import Q

###
# Match
###
class MatchManager(models.Manager):
	 def get_next_for_team(self, team):
	 	return super(MatchManager, self).get_queryset().filter(Q(team_home=team) | Q(team_away=team)).filter(date__gt=datetime.now()).order_by('date')[:1].get()