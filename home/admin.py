from django.contrib import admin
from .models import MenuItem,Order 

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    search_fields = ('name',)
    list_filter = ('price',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','total_amount','order_status','created_at')
    list_filter = ('order_status','created_at')
    search_fields = ('customer__useranme',)
    filter_horizontal = ('order_items',)    

