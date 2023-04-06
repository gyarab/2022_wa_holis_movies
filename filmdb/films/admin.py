from django.contrib import admin

from .models import Movie, Director


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['genres', 'year']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
