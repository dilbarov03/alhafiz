from modeltranslation.translator import TranslationOptions, register
from .models import News, Service

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
    

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)
