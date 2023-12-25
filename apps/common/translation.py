from modeltranslation.translator import TranslationOptions, register
from .models import News, Service, Tarif, Transport

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
    

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Transport)
class TransportTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'body')


@register(Tarif)
class TarifTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
