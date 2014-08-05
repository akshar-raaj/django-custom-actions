from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.contrib import messages


from .models import Instrument

# Register your models here.

def update_price(modeladmin, request, queryset):
    price = request.POST['price']
    price = int(price)
    queryset.update(price=price)
    modeladmin.message_user(request, ("Successfully updated price for %d rows") % (queryset.count(),), messages.SUCCESS)
update_price.short_description = 'Update price of selected rows'


class UpdateActionForm(ActionForm):
    price = forms.IntegerField(required=False)

class InstrumentAdmin(admin.ModelAdmin):
    action_form = UpdateActionForm
    actions = [update_price]

admin.site.register(Instrument, InstrumentAdmin)
