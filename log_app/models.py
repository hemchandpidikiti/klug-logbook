from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager, UserManager
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Attende(models.Model):
    #room_name = models.CharField(max_length=4, blank=False, default='C424')
    uid = models.IntegerField(validators=[MinValueValidator(1000)], blank=False)
    purpose = models.CharField(max_length=12, blank=False)
    date = models.DateField(auto_now_add=True)
    in_time = models.TimeField(auto_now_add=True, null=False)
    out_time = models.TimeField(null=True)

'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.IntegerField(validators=[MinValueValidator(1000)], blank=False)

    def __str__(self):
        return self.user.username'''