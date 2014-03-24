from django.contrib import admin
from .models import *

###
# Inlines
###
class SkillAdmin(admin.TabularInline):
    model = Skill

class PlayerSkillAdmin(admin.TabularInline):
    model = PlayerSkill


###
# Main admin models 
###
class ChampionshipAdmin(admin.ModelAdmin): 
	model = Championship
admin.site.register(Championship, ChampionshipAdmin)

class TeamAdmin(admin.ModelAdmin): 
	model = Team
admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin): 
	model = Player
	inlines = [
		PlayerSkillAdmin
	]
admin.site.register(Player, PlayerAdmin)

class PositionAdmin(admin.ModelAdmin): 
	model = Position
admin.site.register(Position, PositionAdmin)

class SkillTypeAdmin(admin.ModelAdmin): 
	model = SkillType
	inlines = [
        SkillAdmin,
    ]
admin.site.register(SkillType, SkillTypeAdmin)


