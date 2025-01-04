from django.contrib import admin
from .models import Meetinglist,Users,Dept,Attendee

# 注册模型
admin.site.register(Meetinglist)
admin.site.register(Users)
admin.site.register(Dept)
admin.site.register(Attendee)


