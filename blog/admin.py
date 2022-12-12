from django.contrib import admin
from .models import Psychologist




# Register your models here.

admin.site.site_header = "الصفحة الرئيسية للآدمن"
admin.site.site_title = "Admin of saber"


class TopicAdmin(admin.ModelAdmin):
    list_display = ('p_email' , 'req_status')
    list_filter = ('req_status' , 'p_email' )



admin.site.register(Psychologist , TopicAdmin)