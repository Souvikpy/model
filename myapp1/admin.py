from django.contrib import admin
from myapp1 import models
# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)

class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name','url')
    list_editable=('name','url',)
    list_filter=('topic',)


class AccessdetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('webpage','datetime')
    
admin.site.register(models.topic,TopicAdminView)
admin.site.register(models.webpage,WebpageAdminView)
admin.site.register(models.accessDetails,AccessdetailsAdminView)