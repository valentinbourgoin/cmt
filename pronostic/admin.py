from django.contrib import admin

from pronostic.models import *

class MatchDayAdmin(admin.ModelAdmin): 
	model = MatchDay
admin.site.register(MatchDay, MatchDayAdmin)

class MatchAdmin(admin.ModelAdmin): 
	model = Match
	list_display = ('team_home', 'team_away', 'match_day',)
admin.site.register(Match, MatchAdmin)