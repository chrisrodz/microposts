from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    def __unicode__(self):
        return self.post

    post = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateField(blank=True,null=True)