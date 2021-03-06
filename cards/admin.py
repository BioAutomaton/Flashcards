from django.contrib import admin

from .models import Pack, Flashcard, Like, User


class PackAdmin(admin.ModelAdmin):
    fields = ['author', 'title']


class FlashcardAdmin(admin.ModelAdmin):
    fields = ['pack', 'front_side', 'flip_side']


class LikeAdmin(admin.ModelAdmin):
    fields = ['pack', 'user']


# Register your models here.
admin.site.register(Pack, PackAdmin)
admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Like, LikeAdmin)
