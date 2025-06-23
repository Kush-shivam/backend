from django.contrib import admin
from .models import*
# Register your models here.
class AdminContactDetails(admin.ModelAdmin):
    list_display = ['id','name','phoneno','email','messege']
                     

admin.site.register(ContactDetails,AdminContactDetails)  