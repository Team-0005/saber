from django.contrib import admin
from .models import Psychologist




# Register your models here.

admin.site.site_header = "الصفحة الرئيسية للآدمن"
admin.site.site_title = "Admin of saber"


class TopicAdmin(admin.ModelAdmin):
    list_display = ('p_email' , 'req_status' , 'descreption')
    list_filter = ('req_status', 'p_email' )

    def descreption(self, obj):
        if obj.req_status == 1 :
            return "في الانتظار"
        else:
            return "تم الرد"
    def req_status(self, obj):
        if self.req_status == 1 :
            return "في الانتظار"
        else:
            return "تم الرد"


admin.site.register(Psychologist , TopicAdmin)