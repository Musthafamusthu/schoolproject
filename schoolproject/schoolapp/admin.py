from django.contrib import admin
from .models import login
from schoolapp .models import Detailsmodel,Department,Course
# Register your models here.
admin.site.register(login)
admin.site.register(Detailsmodel)
admin.site.register(Department)
admin.site.register(Course)
