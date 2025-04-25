from django.contrib import admin

from .models import Foul, Game, Game_Foul, League, Season, Team

# Register your models here.

admin.site.register(Game)
admin.site.register(Foul)
admin.site.register(Game_Foul)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Season)
