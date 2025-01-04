from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import MemoryJobStore
import pandas as pd
import logging
from meet.models import Meetinglist,Attendee,Users
import requests
from django.utils import timezone
# 设置日志
logger = logging.getLogger('myapp.tasks')
logger.setLevel(logging.INFO)
# 创建文件处理器
file_handler = logging.FileHandler('myapp.log',encoding='utf-8')
file_handler.setLevel(logging.INFO)
# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def qindao_meeting_status():
    try:
        today_date = datetime.now().date()

        # 查询所有用户和会议
        users = Users.objects.all()
        meetlist = Meetinglist.objects.filter(date=today_date)

        # 使用列表推导式避免多个for循环，减少内存消耗
        lis = [
            {
                'meetname': meet.title,
                'user': user.name,
                'meetdate': meet.date,
                'check_time': meet.starttime,
                'status': '签到',
            }
            for meet in meetlist
            for user in users
            if meet.dept_id == user.dept_id
        ]

        # 根据 user, meetname 和 meetdate 来去重
        unique_lis = []
        seen = set()

        for dic in lis:
            unique_key = (dic['user'], dic['meetname'], dic['meetdate'])
            if unique_key not in seen:
                seen.add(unique_key)
                unique_lis.append(dic)

        # 如果列表为空，直接返回
        if not unique_lis:
            return

        # 检查是否已有相同记录，如果有则跳过
        for dic in unique_lis:
            if not Attendee.objects.filter(
                user=dic['user'],
                meetname=dic['meetname'],
                meetdate=dic['meetdate']
            ).exists():
                Attendee.objects.create(**dic)

    except Exception as e:
        raise  # 重新抛出异常以便进一步处理





def start():
    qindao_meeting_status()
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(MemoryJobStore(), "default")

    # 定时任务每2分钟执行一次
    scheduler.add_job(
        qindao_meeting_status,
        "interval",  # 使用间隔调度
        minutes=1,  # 每2分钟执行一次
        id="qindao_meeting_status",
    )

    scheduler.start()
    logger.info("qindao_meeting_status Scheduler started successfully")



