from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notes(models.Model):
    creation_date = models.DateTimeField('date published', auto_now=True)
    content = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner) + "writes:" + self.content
