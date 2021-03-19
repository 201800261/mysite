from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    pub_date = models.DateTimeField('date published',auto_now_add=True, blank=True)
    mod_date = models.DateTimeField('date modified', auto_now=True )
    content = models.TextField()

    #renames the instances of the model
    def __str__(self):
        return "{}".format(self.title)