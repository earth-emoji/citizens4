import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

class PoliticalParty(models.Model):
    name = models.CharField(max_length=120)
    established = models.PositiveIntegerField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Political Parties')

    def __str__(self):
        return self.name

class UserProfileManager(models.Manager):
    use_for_related_fields = True

# Create your models here. 
class UserProfile(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    # contacts    = models.ManyToManyField('self', related_name='contacts', blank=True)    
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    objects = UserProfileManager()

    def __str__(self):
        return self.user.username
