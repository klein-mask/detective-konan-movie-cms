from django.contrib import admin
from app.models import Movie


class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'release_date',)
	list_display_links = ('title',)


admin.site.register(Movie, MovieAdmin)
