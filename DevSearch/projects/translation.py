from modeltranslation.translator import register,TranslationOptions
from .models import Project,Tag,Review

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields=('title','description')

@register(Review)
class ReviewTranslationOPtions(TranslationOptions):
    fields=('body',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields=('name',)