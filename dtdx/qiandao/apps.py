from django.apps import AppConfig
from meeting.settings import ENABLE_SCHEDULED_TASKS

class QiandaoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "qiandao"



    # def ready(self):
    #     # 导入并启动定时任务
    #     from qiandao.scheduler import start
    #     if ENABLE_SCHEDULED_TASKS:
    #         start()



