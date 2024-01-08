from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import News, Gallery, Service, Hotel, Slide, Transport, Tarif, TarifPricing, TarifService, Application


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


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'star', 'distance')
    list_filter = ('star', )
    search_fields = ('name', )
    

@admin.register(Transport)
class TransportAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('created_at', )
    search_fields = ('title', 'subtitle')
    

class TarifPricingInline(admin.TabularInline):
    model = TarifPricing
    extra = 0
    

class TarifServiceInline(admin.TabularInline):
    model = TarifService
    extra = 0
    

@admin.register(Tarif)
class TarifAdmin(TranslationAdmin):
    list_display = ('title', 'start_time', 'end_time', 'days_in_Makkah', 'days_in_Madinah', 'Makkah_hotel', 'Madinah_hotel', 'transport', 'order')
    list_filter = ('created_at', )
    search_fields = ('title', 'body')
    inlines = [TarifPricingInline, TarifServiceInline]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', 'phone')


@admin.register(Slide)
class SlideAdmin(TranslationAdmin):
    list_display = ('title', 'order')
    list_editable = ('order', )
    list_filter = ('created_at', )
    search_fields = ('title', )
