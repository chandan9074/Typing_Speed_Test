from django.db import models
from django.db.models.deletion import CASCADE

from accounts.models import UserProfile


# Create your models here.

class Quotes(models.Model):
    level = models.IntegerField()
    quote = models.TextField()

    def __str__(self):
        return  str(self.level)


class Records(models.Model):
    easy = models.IntegerField(blank=True)
    medium = models.IntegerField(blank=True)
    hard = models.IntegerField(blank=True)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.userProfile.username)
