from django.contrib import admin
from accounts.models import CustomUser,Eventregisterationuser,Webregister,Coupon,AddOnServices,LaboratoryModule,pharamcytab,ModuleMaster

admin.site.register(CustomUser)

class Eventregisteradmin(admin.ModelAdmin):
    list_filter = ['id']


admin.site.register(Eventregisterationuser,Eventregisteradmin)

class WebregisterAdmin(admin.ModelAdmin):
    list_display = ['eventtitle','id','organizedby']
    list_filter = ['id']
admin.site.register(Webregister,WebregisterAdmin)

admin.site.register(Coupon)

