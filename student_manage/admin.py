from django.contrib import admin
from .models import Student

/*creating a registration for our model*/
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.get_fields()]
