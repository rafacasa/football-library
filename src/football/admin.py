from django.contrib import admin

from .models import Foul, Game, Game_Foul, League, Season, Team

# Register your models here.


class GameInline(admin.TabularInline):
    model = Game


class SeasonAdmin(admin.ModelAdmin):
    inlines = [GameInline]


class GameAdmin(admin.ModelAdmin):
    # date_hierarchy = "date"
    fields = [
        "league",
        "season",
        ("home_team", "home_team_score"),
        ("away_team", "away_team_score"),
        "date",
        "video_link",
    ]
    list_display = [
        "date",
        "home_team",
        "home_team_score",
        "away_team_score",
        "away_team",
        "league",
        "season",
    ]
    list_display_links = [
        "date",
        "home_team",
        "home_team_score",
        "away_team_score",
        "away_team",
        "league",
        "season",
    ]
    list_filter = ["league", "season"]


admin.site.register(Game, GameAdmin)
admin.site.register(Foul)
admin.site.register(Game_Foul)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Season, SeasonAdmin)
