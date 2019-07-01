import uuid
from django.db import models

from accounts.models import UserProfile

class Organization(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    founder = models.ForeignKey(UserProfile, related_name="organizations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_member_count(self):
        return self.members.all().count()

class Membership(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    person = models.ForeignKey(UserProfile, related_name='memberships', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='members', on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

class OrganizationRequest(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    organization = models.ForeignKey(Organization, related_name='org_requests', on_delete=models.CASCADE)
    prospect = models.ForeignKey(UserProfile, related_name='org_requests', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class Issue(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='issues')

    def __str__(self):
        return self.name
