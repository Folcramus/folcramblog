from django.contrib import admin

from .models import *



class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]


    class Meta:
        model = News



admin.site.register(News, NewsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]


    class Meta:
        model = Comments



admin.site.register(Comments, CommentsAdmin)


