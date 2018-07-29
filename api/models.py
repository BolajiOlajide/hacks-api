from uuid import uuid4
from django.db import models


# Create your models here.
class Location(models.Model):
	locationId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	location = models.CharField(max_length=100, unique=True, blank=False, null=False)
	country = models.CharField(max_length=100, blank=False, null=False)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return "Location: {}".format(self.location)


class Tag(models.Model):
	tagId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	tag = models.CharField(max_length=150, unique=True, blank=False, null=False)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return "Tag: {}".format(self.tag)


class Hack(models.Model):
	hackId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=100, unique=True, blank=False, null=False)
	description = models.TextField(max_length=1024, blank=False, null=False)
	tag = models.ManyToManyField(Tag)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return "Hacks: {}".format(self.name)
