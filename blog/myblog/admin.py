from django.contrib import admin
from myblog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title',]
    lis_filter=['Revise_time','category']

class CategoryAdmin(admin.ModelAdmin):
    list_disaplay=['name','time']

class IntroduceAdmin(admin.ModelAdmin):
    list_display=['title',]

class photoupdataAdmin(admin.ModelAdmin):
    list_disaplay=['photo_name',]

admin.site.register(UserProfile)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Introduce,IntroduceAdmin)
admin.site.register(photoupdata,photoupdataAdmin)