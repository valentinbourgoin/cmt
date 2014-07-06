from django.shortcuts import render_to_response
from django.template import RequestContext

from core.models import TeamSite
from pronostic.models import Match

###
# Matchday 
###
def matchday(request):
	# Get current team
	team = TeamSite.objects.get_current().team

	# Get next match
	match = Match.objects.get_next_for_team(team)

	return render_to_response('pronostic/matchday.html', {'team': team, 'match': match}, context_instance=RequestContext(request))

