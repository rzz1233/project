from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import MemoryJobStore
import pandas as pd
import logging
from meet.models import MechanicsOnlineDayTest,Meetinglist,Attendee
import requests
from django.utils import timezone





# def sync_clue_to_mechanics():
#     logger.info("sync_clue_to_mechanics...")
#
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # 获取昨天的日期
#     yesterday = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
#
#     url = "http://10.18.41.229:18085/service/serviceinterface/search/run.action"
#     params = {
#         "token": "9bc47b9636af2d76dd3a9ec9168a23d1",
#         "interfaceId": "475872ce7c006363e998246f2c309d72",
#         "START_TIME": yesterday,
#         "END_TIME": yesterday
#     }
#
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json().get("data", [])
#         county_dic = {"北京市":1,  "海淀区":2, "朝阳区":3, "大兴区":4, "房山区":5, "石景山区":6, "东城区":7, "西城区":8, "平谷区":9, "密云区":10, "怀柔区":11, "顺义区":12, "门头沟区":13, "通州区":14, "昌平区":15, "延庆区":16, "丰台区":17}
#
#         for item in data:
#             county_name = item.get("REGION_NAME")
#             county_id = county_dic.get(county_name, None)
#             # 检查是否已有相同的记录（datetime 和 county_id）
#             if not MechanicsOnlineDayTest.objects.filter(
#                     datetime=datetime.strptime(item.get("DATETIME") + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
#                     county_id=county_id).exists():
#                 MechanicsOnlineDayTest.objects.create(
#                     county=county_name,
#                     online_num=item.get("ZXSL"),
#                     zongliangtongbi=None,
#                     zonglianghuanbi=None,
#                     pingjungongshi=item.get("PJGS"),
#                     gongshitongbi=None,
#                     gongshihuanbi=None,
#                     kaigonglv=item.get("KGL"),
#                     kaigonglvtongbi=None,
#                     kaigonglvhuanbi=None,
#                     gongzuoyebili=item.get("GZYBL"),
#                     kaigongshu=item.get("KGSL"),
#                     zonggongshi=item.get("ZGS"),
#                     gaogongzuoyeshu=item.get("GZYS"),
#                     datetime=datetime.strptime(item.get("DATETIME") + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
#                     county_id=county_id
#                 )
#                 logger.info(f"数据保存成功: {county_name} {item.get('DATETIME')}")
#             else:
#                 logger.info(f"数据已存在, 跳过保存: {county_name} {item.get('DATETIME')}")
#
#     except requests.RequestException as e:
#         logger.error(f"请求失败: {e}")

# 设置日志
logger = logging.getLogger('myapp.tasks')
logger.setLevel(logging.INFO)
# 创建文件处理器
file_handler = logging.FileHandler('myapp.log')
file_handler.setLevel(logging.INFO)
# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
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



