from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import *
from . forms import *




class PackageInline(admin.TabularInline):
    model = Package

# class TicketAdmin(admin.ModelAdmin):
#     inlines = [ReservationInline]
#     list_display = ('id','first_name','last_name','phone_number','event')
#     search_fields = ['first_name','phone_number']
#     list_display_links = ['first_name', 'id']
#     list_filter = ['event']
    
    
class PackageAdmin(admin.ModelAdmin):
    list_display = ['id','name_event',]
    search_fields = ['name_event']
    list_display_links = ['name_event', 'id']
   
    

     
    
class TicketNumberAdmin(admin.ModelAdmin):
    list_display = ['id','ticket', 'ticket_number', 'expired']
    search_fields = ['ticket','ticket_number']
    list_display_links = ['ticket', 'id']
    list_filter = ['ticket_number']
    
    
    
class HallAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'hall_price']
    search_fields = ['name','capacity']
    list_display_links = ['name', 'id']
    list_filter = ['hall_price']
  

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','is_admin']

class LaundryAdmin(admin.ModelAdmin):
    list_display    = ['id', 'customer_name', 'commission']
#   
    
# Register your models here.
admin.site.register(Package,PackageAdmin)


admin.site.register(Members)
admin.site.register(Laundry)
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

admin.site.register(TicketNumber,TicketNumberAdmin)
# admin.site.register(ReservationInline)
# admin.site.register()



