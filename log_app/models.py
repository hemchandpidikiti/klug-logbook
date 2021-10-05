from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Attende(models.Model):
    room_name = models.CharField(max_length=4, blank=False, default='C424')
    uid = models.IntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)], blank=False)
    purpose = models.CharField(max_length=12, blank=False)
    date_in_time = models.DateTimeField(auto_now_add=True, null=False)
    date_out_time = models.DateTimeField(null=True)