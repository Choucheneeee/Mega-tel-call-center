from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime, timedelta


class User(AbstractUser):
    id= models.AutoField(primary_key=True)
    GENDER_CHOICES = [
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    ]
    status_choices = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    iposte = [
       ('Admin', 'Admin'),
       ('Employee', 'Employee'),
    ]
    s_type =[
        ('Hourly','Hourly'),
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
    ]
    p_type =[
        ('Bank transfer','Bank transfer'),
        ('Check','Check'),
        ('Cash','Cash'),
    ]

    telephone = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(upload_to='images/')
    adresse = models.CharField(max_length=20,blank=True,null=True)
    Bank_name = models.CharField(max_length=20,blank=True,null=True)
    salair_type =models.CharField(max_length=80, choices=s_type, blank=True, null=True)
    salair_month=models.CharField(max_length=20,blank=True,null=True)
    Payment_type=models.CharField(max_length=80, choices=p_type, blank=True, null=True)
    nationality = models.CharField(max_length=20,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    passport = models.CharField(max_length=20)
    cin = models.CharField(max_length=20)
    date_birthday = models.DateField(blank=True, null=True)
    poste = models.CharField(max_length=80, choices=iposte, blank=True,default='employee', null=True)
    status = models.CharField(max_length=8, choices=status_choices, blank=True, null=True,default='Inactive')
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')
    
    



    def is_last_login_recent(self):
        """
        Check if the user's last login was within the last 2 minutes.
        """
        last_login_time = self.last_login
        if not last_login_time:
            return False

        # Calculate the time difference
        current_time = timezone.now()
        time_difference = current_time - last_login_time

        # Set the threshold for "recent" (e.g., 2 minutes)
        recent_threshold = timedelta(minutes=30)

        return time_difference <= recent_threshold

    def status_as_points(self, *args, **kwargs):
        """
        Determine the user's status based on last login time.
        """
        if self.is_last_login_recent():
            self.status='Active'
            super().save(*args, **kwargs)
            return 'Active'
        else:
            self.status='Inactive'
            super().save(*args, **kwargs)
            return 'Inactive'
    
    
        
    def __int__(self):
        return self.id
    
    
    
from django.db import models
from django.utils import timezone

class Project(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='Project Name')
    description = models.TextField(verbose_name='Project Description')
    
    # Project status
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Planning', verbose_name='Project Status')
    

    def status_as_points(self):
        status_points = {
            'Planning': 10,
            'Ongoing': 70,
            'Completed': 100,
            'On Hold': 50,
        }
        return status_points[self.status]

    start_date = models.DateField(default=timezone.now, verbose_name='Start Date')
    end_date = models.DateField(null=True, blank=True, verbose_name='End Date')
    contact_name = models.CharField(max_length=100, verbose_name='Contact Name')
    contact_email = models.EmailField(verbose_name='Contact Email')
    contact_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Contact Phone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def total_hours(self):
        delta = self.end_date - self.start_date
        hours = delta.total_seconds() / 3600
        return hours
    def __int__(self):
        return self.id
    
    
class ChatGroup(models.Model):
    group_name=models.CharField(max_length=128,unique=True)
    
    def __str__(self):
        return self.group_name

    
class GroupMessage(models.Model):
    group=models.ForeignKey(ChatGroup, related_name='chat_messages' ,on_delete=models.CASCADE)
    author=models.ForeignKey(User ,on_delete=models.CASCADE)
    body=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    
    class Meta:
        ordering = ['-created']
        


from django.db import models
 
# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"
    