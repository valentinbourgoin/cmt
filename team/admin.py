from django.contrib import admin
from .models import *

###
# Inlines
###
class SkillAdmin(admin.TabularInline):
    model = Skill

class PlayerSkillAdmin(admin.TabularInline):
    model = PlayerSkill

class PlayerPositionAdmin(admin.TabularInline):
	model = PlayerPosition


###
# Main admin models 
###
class ChampionshipAdmin(admin.ModelAdmin): 
	model = Championship
admin.site.register(Championship, ChampionshipAdmin)

class TeamAdmin(admin.ModelAdmin): 
	model = Team
	list_display = ('name', 'championship',)
admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin): 
	model = Player
	list_display = ('firstname', 'lastname', 'get_main_position')
	list_filter = ('team', 'positions')
	inlines = [
		PlayerSkillAdmin,
		PlayerPositionAdmin,
	]
admin.site.register(Player, PlayerAdmin)

class PositionAdmin(admin.ModelAdmin): 
	model = Position
	list_display = ('label', 'type',)
admin.site.register(Position, PositionAdmin)

class SkillTypeAdmin(admin.ModelAdmin): 
	model = SkillType
	inlines = [
        SkillAdmin, 
    ]
admin.site.register(SkillType, SkillTypeAdmin)

class SkillFullAdmin(admin.ModelAdmin):
	list_display = ('label', 'type',)
	model = Skill
admin.site.register(Skill, SkillFullAdmin)
