from django.contrib import admin

from .models import Categories, Materials


admin.site.register(Categories)
admin.site.register(Materials)
admin.site.empty_value_display = 'Не задано'
