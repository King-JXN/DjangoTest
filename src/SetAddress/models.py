from django.db import models
from django.contrib import admin

# Create your models here.
class SetAddressPostInfor(models.Model):
    infor = models.CharField(max_length=150)
    displayInfor = models.TextField()

class SetAddressPostAdmin(admin.ModelAdmin):
    list_display = ('infor', 'displayInfor')
    
admin.site.register(SetAddressPostInfor, SetAddressPostAdmin)