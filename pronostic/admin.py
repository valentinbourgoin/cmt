from django.contrib import admin

from pronostic.models import *

class MatchDayAdmin(admin.ModelAdmin): 
	model = MatchDay
admin.site.register(MatchDay, MatchDayAdmin)