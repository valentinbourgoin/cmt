from django.contrib import admin

from models import *

class TeamSiteAdmin(admin.ModelAdmin): 
	model = TeamSite
admin.site.register(TeamSite, TeamSiteAdmin)

class SponsorAdmin(admin.ModelAdmin): 
	model = Sponsor
admin.site.register(Sponsor, SponsorAdmin)