from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
  model = User
  list_display = ["email","name","nid"]
admin.site.register(User,UserAdmin)
# Register your models here.
