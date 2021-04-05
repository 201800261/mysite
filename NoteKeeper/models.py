from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    pub_date = models.DateTimeField('date published',auto_now_add=True, blank=True)
    mod_date = models.DateTimeField('date modified', auto_now=True )
    content = models.TextField()

    #renames the instances of the model

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return "{}".format(self.title)

