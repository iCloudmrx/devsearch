from modeltranslation.translator import register,TranslationOptions
from .models import Profile,Skill,Message

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields=('name','location','short_intro','bio')

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields=('name','description')

@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields=('name','subject','body')