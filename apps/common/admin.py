from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline

from .models import News, Gallery, Service


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', )
    search_fields = ('title', 'body')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'youtube_link', 'order')
    list_editable = ('order', )
    list_filter = ('created_at', )
    

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', )
    list_filter = ('created_at', )
    search_fields = ('name', )
