from django.contrib import admin

from .models import Tehtava

class TehtavaAdmin(admin.ModelAdmin):
    fields = ["otsikko"]

admin.site.register(Tehtava, TehtavaAdmin)