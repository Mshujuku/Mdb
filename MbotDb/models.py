from django.db import models

# Create your models here.

class MbotDb(models.Model):
    msg_id = models.CharField(max_length=100)
    msg_time_rec = models.DateTimeField(auto_now_add =True)
    msg_group_name = models.CharField(max_length=100)
    msg_from_user = models.CharField(max_length=100)
    msg_content = models.TextField()
    msg_create_time = models.DateTimeField(auto_now_add =True)
    msg_type = models.CharField(max_length=100)

