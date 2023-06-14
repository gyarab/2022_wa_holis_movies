from django.contrib import admin

from .models import Movie, Director, Actor, Genre


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['genres', 'year', 'director']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_year']
    list_display_links = ['name']
    search_fields = ['name', 'birth_year', 'movie__name']
    list_filter = ['birth_year']
    inlines = [MovieInline]


class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_year']
    list_display_links = ['name']
    search_fields = ['name', 'birth_year', 'movies__name']
    list_filter = ['birth_year']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)
