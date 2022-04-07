from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('work', views.work, name="work"),
#     path('request', views.request, name="request"),
#     path('notice', views.notice, name="notice"),
#     path('attendance', views.attendance, name="attendance"),
# ]   
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('attendance',views.attendance,name="attendance"),
    path('notice',views.notice,name="notice"),
    path('noticedetail/?P<id>/',views.noticedetail,name="noticedetail"),
    path('assignwork',views.assignWork,name="assignwork"),
    path('mywork',views.mywork,name="mywork"),
    path('workdetails/?P<wid>/',views.workdetails,name="workdetails"),
    path('editAW',views.assignedworklist,name="assignedworklist"),
    path('deletework/?P<wid>/',views.deletework,name="deletework"),
    path('updatework/?P<wid>',views.updatework,name="updatework"),
    path('makeRequest',views.makeRequest,name="makeRequest"),
    path('viewRequest',views.viewRequest,name="viewRequest"),
    path('requestdetails/?P<rid>/',views.requestdetails,name="requestdetails"),
]