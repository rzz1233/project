from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import MemoryJobStore
import pandas as pd
import logging
from meet.models import MechanicsOnlineDayTest,Meetinglist,Attendee
import requests
from django.utils import timezone
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取项目根目录并确保 logs 文件夹存在
log_dir = os.path.join(BASE_DIR, "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 创建日志记录器
logger = logging.getLogger('myapp.tasks')
logger.setLevel(logging.INFO)  # 设置日志级别

# 创建文件处理器（日志文件路径可以动态生成）
log_file_path = os.path.join(log_dir, 'myapp.log')

# 创建文件处理器，设置日志级别
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)

# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将文件处理器添加到日志记录器
logger.addHandler(file_handler)

def update_meeting_status():
    # 获取本地时间
    current_datetime = timezone.localtime(timezone.now())
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    logger.info(f"当前时间: {current_datetime} - 开始更新会议状态")

    # 更新已过期的会议状态
    expired_meetings = Meetinglist.objects.filter(
        date__lt=current_date,
        status__in=['未开始', '进行中']  # 同时更新未开始和进行中的过期会议
    )
    expired_count = expired_meetings.update(status='已结束')
    logger.info(f"更新了 {expired_count} 个已过期会议的状态为 '已结束'")

    # 更新当天的会议状态
    today_meetings = Meetinglist.objects.filter(
        date=current_date
    )

    updated_count = 0
    for meeting in today_meetings:
        # 严格的时间比较
        if meeting.starttime <= current_time <= meeting.endtime:
            if meeting.status != '进行中':
                meeting.status = '进行中'
                meeting.save()
                updated_count += 1
                logger.info(f"会议 {meeting.title} 状态更新为 '进行中'")
        elif current_time > meeting.endtime:
            if meeting.status != '已结束':
                meeting.status = '已结束'
                meeting.save()
                updated_count += 1
                logger.info(f"会议 {meeting.title} 状态更新为 '已结束'")
        elif current_time < meeting.starttime:
            if meeting.status != '未开始':
                meeting.status = '未开始'
                meeting.save()
                updated_count += 1
                logger.info(f"会议 {meeting.title} 状态更新为 '未开始'")

    if updated_count == 0:
        logger.info("今天没有需要更新的会议状态")
    else:
        logger.info(f"已更新 {updated_count} 个会议的状态")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(MemoryJobStore(), "default")

    # 定时任务每2分钟执行一次
    scheduler.add_job(
        update_meeting_status,
        "interval",  # 使用间隔调度
        minutes=2,  # 每2分钟执行一次
        id="update_meeting_status",
    )

    scheduler.start()
    logger.info("Scheduler started successfully")



