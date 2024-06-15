from django.contrib import admin
from .models import *
# Register your models here.

class User_admin(admin.ModelAdmin):
    list_display = ("id","username", "telephone", "poste","cin","gender","created_at","status")

class Project_admin(admin.ModelAdmin):
    list_display = ("id","name", "status", "start_date","end_date","created_at","updated_at")
        
class ChatGroup_admin(admin.ModelAdmin):
    list_display = ("group_name",)

class GroupMessage_admin(admin.ModelAdmin):
    list_display = ("group","author","body","created")      
    
admin.site.register(User, User_admin)
admin.site.register(ChatGroup, ChatGroup_admin)
admin.site.register(GroupMessage, GroupMessage_admin)

admin.site.register(Project,Project_admin)

class Events_admin(admin.ModelAdmin):
    list_display = ("id","name","start","end")
admin.site.register(Events, Events_admin) 