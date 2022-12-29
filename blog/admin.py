from django.contrib import admin
from .models import Psychologist


# Register your models here.

admin.site.site_header = "الصفحة الرئيسية للآدمن"
admin.site.site_title = "Admin of saber"


class TopicAdmin(admin.ModelAdmin):
    list_display = ('p_email', 'descreption',
                    'req_status', 'p_l_name', 'p_f_name')
    list_filter = ('req_status', 'current_job_title')

    def descreption(self, obj):
        if obj.req_status == 0:
            return "في الانتظار"
        else:
            return "تم الرد"


admin.site.register(Psychologist, TopicAdmin)
