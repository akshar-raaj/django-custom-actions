from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms

from .models import Instrument

# Register your models here.

class UpdateActionForm(ActionForm):
    price = forms.IntegerField(required=False)

class InstrumentAdmin(admin.ModelAdmin):
    action_form = UpdateActionForm

admin.site.register(Instrument, InstrumentAdmin)
