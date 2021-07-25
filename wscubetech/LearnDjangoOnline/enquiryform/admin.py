from django.contrib import admin
from enquiryform.models import Enquiry

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(Enquiry, EnquiryAdmin)
