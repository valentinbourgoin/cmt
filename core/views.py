from django.shortcuts import render_to_response
from django.template import RequestContext

from core.models import TeamSite
from pronostic.models import Match

###
# Homepage
###
def homepage(request):
	# Get current team
	team = TeamSite.objects.get_current().team

	# Get next match (and opposant to current team)
	match = Match.objects.get_next_for_team(team)
	opposant = match.get_opposant(team)

	# Get sponsors 
	sponsors = TeamSite.objects.get_current().sponsor_set.all()

	# Render view
	return render_to_response(
		'core/homepage.html', 
		{
			'team': team, 
			'match': match, 
			'opposant': opposant, 
			'sponsors': sponsors
		}, 
		context_instance=RequestContext(request)
	)