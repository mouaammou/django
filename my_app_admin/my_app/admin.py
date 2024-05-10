from django.contrib import admin
from .models import Member

# Register your models here.


class user_display_info(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")


admin.site.register(Member, user_display_info)
