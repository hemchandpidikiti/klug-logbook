from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager, UserManager
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Attende(models.Model):
    #User = settings.AUTH_USER_MODEL
    #user = models.ForeignKey(User, null=True)
    room_name = models.CharField(max_length=12, blank=False, null=False)
    uname = models.CharField(max_length=30, null=True)
    uid = models.IntegerField(validators=[MinValueValidator(1000)], blank=False)
    purpose = models.CharField(max_length=12, blank=False)
    date = models.DateField(auto_now_add=True)
    in_time = models.TimeField(null=True)
    out_time = models.TimeField(null=True)

class Master(models.Model):
    name = models.CharField(max_length=30, null=True)
    rfid_id = models.CharField(max_length=12)
    uid = models.IntegerField(validators=[MinValueValidator(1000)])

    class Meta:
        unique_together = (('rfid_id', 'uid'),)
        index_together = (('rfid_id', 'uid'),)

'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.IntegerField(validators=[MinValueValidator(1000)], blank=False)

    def __str__(self):
        return self.user.username'''