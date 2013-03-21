from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
	def __unicode__(self):
		return self.follower.username
	follower = models.OneToOneField(User)
	following = models.ManyToManyField('self', related_name='+', blank=True, null=True)

class Post(models.Model):
    def __unicode__(self):
        return self.post

    post = models.CharField(max_length=200)
    user = models.ForeignKey(Follower)
    date = models.DateField(blank=True,null=True)
    