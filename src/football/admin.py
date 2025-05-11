from django.contrib import admin

from .models import Foul, Game, Game_Foul, League, Season, Team

# Register your models here.


class GameInline(admin.TabularInline):
    model = Game


class SeasonAdmin(admin.ModelAdmin):
    inlines = [GameInline]


admin.site.register(Game)
admin.site.register(Foul)
admin.site.register(Game_Foul)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Season, SeasonAdmin)
