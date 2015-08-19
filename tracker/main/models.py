from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Area(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='areas')
    date_created = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)


class Point(models.Model):
    area = models.ForeignKey('Area', related_name='points')
    lat = models.FloatField()
    lng = models.FloatField()
    order = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.area)
