from django.contrib import admin

from api.models import Hack, Tag, Location


# Register your models here.
admin.site.register(Hack)
admin.site.register(Tag)
admin.site.register(Location)
