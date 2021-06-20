from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from vacancy.models import S_C, L_C

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=100, blank=True, default='-')
    sex = models.CharField(max_length=30, blank=True, default='-')
    age = models.PositiveSmallIntegerField(blank=True, default=0)
    education = models.CharField(max_length=100, blank=True, default='-')
    group = models.CharField(max_length=100, blank=True, default='-')
    city = models.CharField(max_length=50, blank=True, default='-')
    street = models.CharField(max_length=50, blank=True, default='-')
    move = models.CharField(max_length=10, blank=True, default='-')
    phone = models.CharField(max_length=20, blank=True, default='-')
    job_wish = models.CharField(max_length=300, blank=True, default='')
    profession = models.CharField(max_length=300, blank=True, default='')
    experience = models.CharField(max_length=300, blank=True, default='')
    skills = MultiSelectField(choices=S_C, blank=True)
    limits = MultiSelectField(choices=L_C, blank=True)
    def s_list(self): return str(self.skills).split(',')[:3]
    def l_list(self): return str(self.limits).split(',')[:3]

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()