from . import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin-dashboard.html', views.admin, name='admin'),
    path('employee-dashboard.html',views.employee,name='employee'),
    path('chat.html',views.chat,name="chat"),
    path('profile<int:id>.html', views.profile, name='profile'),
    path('employees.html',views.employ,name='emply'),
    path('project-view<int:id>.html',views.project,name='project'),
    path('project.html',views.allproject,name='project'),
    path('attendance.html',views.att,name='att'),
    path('login.html',views.login_view,name='login'),
    path('project.html',views.allproject,name='contact'),
    path("logout", views.logout_view, name="logout"),
    path('index.html',views.index2,name='index2'),
    path('data.html',views.data,name='data'),
    path('contact.html',views.contact,name='contact'),
    path('aboutUs.html',views.about,name='about'),
    path('calender.html',views.calender,name='calendar'),
    path('create_projects',views.creat,name='creat'),
    path('create_emp',views.createmp,name='createmp'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path("meeting/",views.vedio,name="meeting"),
    path("join/",views.joinvedio,name="joinvedio"),
    path('calender.html', views.index, name='index'), 
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)