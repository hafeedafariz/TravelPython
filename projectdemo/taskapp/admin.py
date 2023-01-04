from django.contrib import admin
from . models import Site
from . models import School
# Register your models here.
admin.site.register(Site)
admin.site.register(School)