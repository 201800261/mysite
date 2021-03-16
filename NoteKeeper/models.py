from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    def __str__(self):
        return "{}.{}".format(self.id, self.title)
