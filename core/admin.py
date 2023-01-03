from django.contrib import admin
from .models import User,Prescription
class UserAdmin(admin.ModelAdmin):
  model = User
  list_display = ["email","name","nid"]
class PrescriptionAdmin(admin.ModelAdmin):
  model = Prescription
  list_display = ["user","title"]
admin.site.register(User,UserAdmin)
admin.site.register(Prescription,PrescriptionAdmin)
# Register your models here.
