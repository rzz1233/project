from meet.views import (UserView,MeetinglistView,AttendeeView,DeptView,
                    MeetinglistDetailView,AttendeeDetailView,register,login,CustomTokenRefreshView,UserListView,QiandaoView)

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
# 创建一个默认的路由器
router = DefaultRouter()
# 注册视图集


router.register("user",UserView)
router.register("dept",DeptView)
router.register("users",UserListView)
router.register("meetinglist",MeetinglistView,basename='meetinglist')
router.register(r'meetinglist1', MeetinglistDetailView, basename='meetinglist1')
router.register("attendee",AttendeeView,basename='attendee')
router.register("attendeepro",AttendeeDetailView,basename='attendeepro')


urlpatterns = [
    path('login/', login, name='login'),  # 登录接口路径
    path('register1/', register, name='register1'),  # 注册接口路径
    path('qiandao/', QiandaoView.as_view(), name='qiandao'),
    # path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 获取 Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新 Token
    path('meetinglist/update-status/', MeetinglistView.as_view({'get': 'update_meeting_status'}), name='meeting-status-update'),
]